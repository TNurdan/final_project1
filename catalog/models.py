from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Position(models.Model):
    """
    Model representing the position of player (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter the position of player (e.g. Central Midfielder, Centarl Defender etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Player(models.Model):
    """
    Model representing the Player .
    """
    Full_name = models.CharField(max_length=200)
    current_club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True)
    nationality =  models.CharField(max_length=100, null = True)
    # Foreign Key used 
    # Player 
    information = models.CharField(max_length=200, help_text="Enter description of the player")
    age = models.CharField('Age',max_length=13, help_text='13 Character <a href="enter age of the player</a>')
    position = models.ForeignKey(Position,  on_delete=models.SET_NULL, null=True, help_text="Select a position of player")
    
    #enter
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Full_name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('player_detail', args=[str(self.id)])
class Club(models.Model):
    """
    Model representing the club
    """
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    trophies = models.CharField(null=True, blank=True, max_length=100)
    information = models.CharField(max_length=1000,  null=True, help_text="Enter description of the player") 
    my_teams = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    @property
    def is_overdue(self):
            return True
    def get_absolute_url(self):
        """
        Returns the url to access a
        """
        return reverse('club-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return (self.name)
    class Meta:
        ordering = ['name']