from django.urls import path
from .views import PlayerAPIView, TeamAPIView, TournamentsAPIView, TournamentAPIView


urlpatterns = [
    path('players/', PlayerAPIView.as_view(), name='player-list'),
    path('teams/<int:pk>', TeamAPIView.as_view(), name='team-list'),
    path('tournaments/', TournamentsAPIView.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>', TournamentAPIView.as_view({'get': 'retrieve', 'patch':'patch', 'delete':'delete'}), name='tournament-details'),
    path('tournaments/<int:pk>/add_team', TournamentAPIView.as_view({'post': 'add_team'}), name='tournament-add-team'),
    path('tournaments/accept_team/<int:pk>', TournamentAPIView.as_view({'post': 'accept_team'}), name='tournament-accept-team')
]