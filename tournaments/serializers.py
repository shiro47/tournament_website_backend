from rest_framework import serializers
from .models import Tournament, Team, Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
    player3 = PlayerSerializer()
    class Meta:
        model = Team
        fields = '__all__'
    
    def create(self, validated_data):
        player1_data = validated_data.pop('player1')
        player2_data = validated_data.pop('player2')
        player3_data = validated_data.pop('player3')

        player1 = Player.objects.create(**player1_data)
        player2 = Player.objects.create(**player2_data)
        player3 = Player.objects.create(**player3_data)

        team = Team.objects.create(player1=player1, player2=player2, player3=player3, **validated_data)
        return team
    
class TournamentSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, required=False)

    class Meta:
        model = Tournament
        fields = '__all__'
