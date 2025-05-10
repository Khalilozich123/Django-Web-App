from django.db import models


class Competition(models.Model):
    """Model for football competitions"""
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    current_season_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Team(models.Model):
    """Model for football teams"""
    team_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    tla = models.CharField(max_length=5, null=True, blank=True)  # Three-letter acronym
    logo_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Standing(models.Model):
    """Model for team standings in competitions"""
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.IntegerField()
    played_games = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    group = models.CharField(max_length=50, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('competition', 'team')

    def __str__(self):
        return f"{self.team.name} - {self.competition.name}"


class Match(models.Model):
    """Model for football matches"""
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('LIVE', 'Live'),
        ('IN_PLAY', 'In Play'),
        ('PAUSED', 'Paused'),
        ('FINISHED', 'Finished'),
        ('POSTPONED', 'Postponed'),
        ('SUSPENDED', 'Suspended'),
        ('CANCELED', 'Canceled'),
    ]

    match_id = models.IntegerField(primary_key=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    matchday = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    utc_date = models.DateTimeField()

    # Scores
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name}"


class Scorer(models.Model):
    """Model for top scorers"""
    player_id = models.IntegerField()
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(null=True, blank=True, default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('player_id', 'competition')

    def __str__(self):
        return f"{self.name} ({self.goals} goals)"