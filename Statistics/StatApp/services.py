from datetime import datetime
import os
import time
import json
import requests
from django.conf import settings
from .models import Competition, Team, Standing, Match, Scorer


class FootballDataService:
    """Service to interact with the football-data.org API"""

    def __init__(self):
        self.api_key = settings.FOOTBALL_API_KEY
        self.base_url = "https://api.football-data.org/v4"
        self.headers = {"X-Auth-Token": self.api_key}
        self.cache_dir = os.path.join(settings.BASE_DIR, 'cache')

        # Create cache directory if it doesn't exist
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get_competitions(self):
        """Get available competitions and save to DB"""
        data = self._make_request("/competitions")
        competitions = data.get('competitions', [])

        saved_competitions = []
        for comp_data in competitions:
            if 'code' not in comp_data:
                continue

            comp, created = Competition.objects.update_or_create(
                code=comp_data['code'],
                defaults={
                    'name': comp_data['name'],
                    'country': comp_data.get('area', {}).get('name', ''),
                    'start_date': comp_data.get('currentSeason', {}).get('startDate'),
                    'end_date': comp_data.get('currentSeason', {}).get('endDate'),
                    'current_season_id': comp_data.get('currentSeason', {}).get('id')
                }
            )
            saved_competitions.append(comp)

        return saved_competitions

    def get_competition_standings(self, competition_code):
        """Get standings for a competition and save to DB"""
        data = self._make_request(f"/competitions/{competition_code}/standings")
        if 'standings' not in data:
            return []

        standings_list = []
        for standing_type in data['standings']:
            group = standing_type.get('group', '')

            for team_standing in standing_type['table']:
                # Get or create team
                team_data = team_standing['team']
                team, _ = Team.objects.update_or_create(
                    team_id=team_data['id'],
                    defaults={
                        'name': team_data['name'],
                        'short_name': team_data.get('shortName'),
                        'tla': team_data.get('tla'),
                        'logo_url': team_data.get('crest')
                    }
                )

                # Create or update standing
                standing, _ = Standing.objects.update_or_create(
                    competition_id=competition_code,
                    team=team,
                    defaults={
                        'position': team_standing['position'],
                        'played_games': team_standing['playedGames'],
                        'won': team_standing['won'],
                        'draw': team_standing['draw'],
                        'lost': team_standing['lost'],
                        'points': team_standing['points'],
                        'goals_for': team_standing['goalsFor'],
                        'goals_against': team_standing['goalsAgainst'],
                        'goal_difference': team_standing['goalDifference'],
                        'group': group
                    }
                )
                standings_list.append(standing)

        return standings_list

    def get_competition_matches(self, competition_code, matchday=None):
        """Get matches for a competition and save to DB"""
        params = {}
        if matchday:
            params['matchday'] = matchday

        data = self._make_request(f"/competitions/{competition_code}/matches", params)
        if 'matches' not in data:
            return []

        matches_list = []
        for match_data in data['matches']:
            # Get or create teams
            home_team, _ = Team.objects.update_or_create(
                team_id=match_data['homeTeam']['id'],
                defaults={
                    'name': match_data['homeTeam']['name'],
                    'short_name': match_data['homeTeam'].get('shortName'),
                    'tla': match_data['homeTeam'].get('tla'),
                    'logo_url': match_data['homeTeam'].get('crest')
                }
            )

            away_team, _ = Team.objects.update_or_create(
                team_id=match_data['awayTeam']['id'],
                defaults={
                    'name': match_data['awayTeam']['name'],
                    'short_name': match_data['awayTeam'].get('shortName'),
                    'tla': match_data['awayTeam'].get('tla'),
                    'logo_url': match_data['awayTeam'].get('crest')
                }
            )

            # Get scores if available
            home_score = None
            away_score = None
            if match_data['status'] in ['FINISHED', 'IN_PLAY', 'PAUSED']:
                if 'score' in match_data and 'fullTime' in match_data['score']:
                    home_score = match_data['score']['fullTime'].get('home')
                    away_score = match_data['score']['fullTime'].get('away')

            # Create or update match
            match, _ = Match.objects.update_or_create(
                match_id=match_data['id'],
                defaults={
                    'competition_id': competition_code,
                    'home_team': home_team,
                    'away_team': away_team,
                    'matchday': match_data.get('matchday'),
                    'status': match_data['status'],
                    'utc_date': datetime.fromisoformat(match_data['utcDate'].replace('Z', '+00:00')),
                    'home_score': home_score,
                    'away_score': away_score
                }
            )
            matches_list.append(match)

        return matches_list

    def get_competition_scorers(self, competition_code, limit=10):
        """Get top scorers for a competition and save to DB"""
        params = {'limit': limit}
        data = self._make_request(f"/competitions/{competition_code}/scorers", params)
        if 'scorers' not in data:
            return []

        scorers_list = []
        for scorer_data in data['scorers']:
            # Get or create team
            team_data = scorer_data['team']
            team, _ = Team.objects.update_or_create(
                team_id=team_data['id'],
                defaults={
                    'name': team_data['name'],
                    'short_name': team_data.get('shortName'),
                    'tla': team_data.get('tla'),
                    'logo_url': team_data.get('crest')
                }
            )

            # Create or update scorer
            scorer, _ = Scorer.objects.update_or_create(
                player_id=scorer_data['player']['id'],
                competition_id=competition_code,
                defaults={
                    'name': scorer_data['player']['name'],
                    'team': team,
                    'goals': scorer_data['goals'],
                    'assists': scorer_data.get('assists', 0)
                }
            )
            scorers_list.append(scorer)

        return scorers_list

    def _make_request(self, endpoint, params=None):
        """Make a request to the API with cache management"""
        cache_file = self._get_cache_filename(endpoint, params)

        # Check if data is in cache and recent (less than an hour)
        if os.path.exists(cache_file):
            file_age = time.time() - os.path.getmtime(cache_file)
            if file_age < 3600:  # 1 hour
                with open(cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)

        # If no valid cache, make the request
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()

            # Save to cache
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

            return data
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            if os.path.exists(cache_file):
                print("Using cached data (potentially outdated)")
                with open(cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return {"error": str(e)}

    def _get_cache_filename(self, endpoint, params=None):
        """Generate a filename for the cache based on endpoint and parameters"""
        # Clean the endpoint for use in a filename
        clean_endpoint = endpoint.replace('/', '_')

        # Add parameters to filename if they exist
        param_str = ""
        if params:
            param_str = "_" + "_".join(f"{k}-{v}" for k, v in params.items())

        return os.path.join(self.cache_dir, f"{clean_endpoint}{param_str}.json")