from django.urls import path
from .views import PlayerAPIView, TeamAPIView, TournamentsAPIView, TournamentAPIView

urlpatterns = [
    path('players/', PlayerAPIView.as_view(), name='player-list'),
    path('teams/', TeamAPIView.as_view(), name='team-list'),
    path('tournaments/', TournamentsAPIView.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>', TournamentAPIView.as_view(), name='tournament-details'),
]