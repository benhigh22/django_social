from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    time_made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name

    class Meta:
        ordering = ['-time_made']

class Topic(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    teams = models.ManyToManyField(Team)


    class Meta:
        ordering = ['-time_created']


