from django.urls import path
from .views import PlayerAPIView, TeamAPIView, TournamentAPIView

urlpatterns = [
    path('players/', PlayerAPIView.as_view(), name='player-list'),
    path('teams/', TeamAPIView.as_view(), name='team-list'),
    path('tournaments/', TournamentAPIView.as_view(), name='tournament-list'),
]