from django.contrib import admin
from .models import Competition, Team, Standing, Match, Scorer


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'country', 'start_date', 'end_date')
    search_fields = ('name', 'country')
    list_filter = ('country',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'name', 'short_name', 'tla')
    search_fields = ('name', 'short_name')


@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ('team', 'competition', 'position', 'played_games', 'won', 'draw', 'lost', 'points', 'goal_difference')
    list_filter = ('competition',)
    search_fields = ('team__name',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'competition', 'home_team', 'away_team', 'status', 'utc_date', 'home_score', 'away_score')
    list_filter = ('competition', 'status', 'matchday')
    search_fields = ('home_team__name', 'away_team__name')
    date_hierarchy = 'utc_date'


@admin.register(Scorer)
class ScorerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'competition', 'goals', 'assists')
    list_filter = ('competition',)
    search_fields = ('name', 'team__name')