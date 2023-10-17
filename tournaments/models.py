from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
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
    isActive = models.BooleanField(default=False, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        self.player1.delete()
        self.player2.delete()
        self.player3.delete()
        super(Team, self).delete(using, keep_parents)

class Tournament(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    rewards = models.TextField(default="")
    rules = models.TextField(default="")
    teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
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
        
    def delete(self, using=None, keep_parents=False):
        self.teams.all().delete()
        super(Tournament, self).delete(using, keep_parents)