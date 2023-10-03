from rest_framework import serializers
from .models import Tournament, Team, Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    player1_name = serializers.CharField(source='player1.name', read_only=True)
    player2_name = serializers.CharField(source='player2.name', read_only=True)
    player3_name = serializers.CharField(source='player3.name', read_only=True)
    class Meta:
        model = Team
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, required=False)

    class Meta:
        model = Tournament
        fields = '__all__'
