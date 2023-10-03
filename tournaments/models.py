from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=50)
    platforms = [
        ("PC", "PC"),
        ("PS4", "Playstation"),
        ("X1", "XBOX")
    ]
    platform = models.CharField(max_length=3, choices=platforms)
    discordID = models.IntegerField()
    discordName = models.CharField(max_length=50)
    rank = models.CharField(max_length=15, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='team_player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='team_player2')
    player3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='team_player3')
    
    def __str__(self) -> str:
        return self.name

class Tournament(models.Model):
    title = models.CharField(max_length=100, default="undefined")
    description = models.TextField(default="undefined")
    rewards = models.TextField(default="undefined")
    rules = models.TextField(default="undefined")
    teams = models.ManyToManyField(Team, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    def clean(self):
        # Check if the number of teams exceeds the limit (20)
        if self.pk is not None:
            if self.teams.count() > 20:
                raise ValidationError("A tournament can have a maximum of 20 teams.")
    
    def save(self, *args, **kwargs):
        # Call the clean method before saving
        self.clean()
        super(Tournament, self).save(*args, **kwargs)