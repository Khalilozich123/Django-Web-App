from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('competition/<str:competition_code>/', views.CompetitionDetailView.as_view(), name='competition_detail'),
    path('competition/<str:competition_code>/matches/', views.MatchesView.as_view(), name='matches'),
    path('competition/<str:competition_code>/scorers/', views.ScorersView.as_view(), name='scorers'),
    path('refresh/', views.RefreshDataView.as_view(), name='refresh_all'),
    path('refresh/<str:competition_code>/', views.RefreshDataView.as_view(), name='refresh_competition'),
]