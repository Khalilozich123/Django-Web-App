from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import Competition, Team, Standing, Match, Scorer
from .services import FootballDataService


class HomeView(View):
    """Home page view"""

    def get(self, request):
        # Get list of competitions
        competitions = Competition.objects.all().order_by('name')

        # Check if we need to refresh data
        if not competitions:
            try:
                service = FootballDataService()
                service.get_competitions()
                competitions = Competition.objects.all().order_by('name')
                messages.success(request, "Competition data refreshed successfully.")
            except Exception as e:
                messages.error(request, f"Error refreshing data: {str(e)}")

        context = {
            'competitions': competitions
        }
        return render(request, 'statapp/home.html', context)


class CompetitionDetailView(View):
    """View for competition details"""

    def get(self, request, competition_code):
        competition = get_object_or_404(Competition, code=competition_code)

        # Get standings for this competition
        standings = Standing.objects.filter(competition=competition).order_by('position')

        # Check if we need to refresh data
        if not standings:
            try:
                service = FootballDataService()
                service.get_competition_standings(competition_code)
                standings = Standing.objects.filter(competition=competition).order_by('position')
                messages.success(request, "Standings data refreshed successfully.")
            except Exception as e:
                messages.error(request, f"Error refreshing standings: {str(e)}")

        context = {
            'competition': competition,
            'standings': standings
        }
        return render(request, 'statapp/competition_detail.html', context)


class MatchesView(View):
    """View for matches"""

    def get(self, request, competition_code):
        competition = get_object_or_404(Competition, code=competition_code)

        # Get matchday filter if provided
        matchday = request.GET.get('matchday')

        # Get matches
        matches_query = Match.objects.filter(competition=competition)
        if matchday and matchday.isdigit():
            matches_query = matches_query.filter(matchday=int(matchday))

        matches = matches_query.order_by('utc_date')

        # Check if we need to refresh data
        if not matches:
            try:
                service = FootballDataService()
                if matchday and matchday.isdigit():
                    service.get_competition_matches(competition_code, int(matchday))
                else:
                    service.get_competition_matches(competition_code)

                # Re-fetch matches
                matches = matches_query.order_by('utc_date')
                messages.success(request, "Match data refreshed successfully.")
            except Exception as e:
                messages.error(request, f"Error refreshing matches: {str(e)}")

        # Get matchday options
        matchday_options = Match.objects.filter(competition=competition).values_list(
            'matchday', flat=True).distinct().order_by('matchday')

        context = {
            'competition': competition,
            'matches': matches,
            'matchday_options': matchday_options,
            'current_matchday': matchday
        }
        return render(request, 'statapp/matches.html', context)


class ScorersView(View):
    """View for top scorers"""

    def get(self, request, competition_code):
        competition = get_object_or_404(Competition, code=competition_code)

        # Get scorers
        scorers = Scorer.objects.filter(competition=competition).order_by('-goals')

        # Check if we need to refresh data
        if not scorers:
            try:
                service = FootballDataService()
                service.get_competition_scorers(competition_code)
                scorers = Scorer.objects.filter(competition=competition).order_by('-goals')
                messages.success(request, "Scorers data refreshed successfully.")
            except Exception as e:
                messages.error(request, f"Error refreshing scorers: {str(e)}")

        context = {
            'competition': competition,
            'scorers': scorers
        }
        return render(request, 'statapp/scorers.html', context)


class RefreshDataView(View):
    """View for manually refreshing data"""

    def get(self, request, competition_code=None):
        try:
            service = FootballDataService()

            if competition_code:
                # Refresh specific competition data
                competition = get_object_or_404(Competition, code=competition_code)
                service.get_competition_standings(competition_code)
                service.get_competition_matches(competition_code)
                service.get_competition_scorers(competition_code)
                messages.success(request, f"Data for {competition.name} refreshed successfully.")
                return redirect(reverse('competition_detail', args=[competition_code]))
            else:
                # Refresh all competitions
                service.get_competitions()
                messages.success(request, "All competitions refreshed successfully.")
                return redirect(reverse('home'))
        except Exception as e:
            messages.error(request, f"Error refreshing data: {str(e)}")
            return redirect(request.META.get('HTTP_REFERER', reverse('home')))