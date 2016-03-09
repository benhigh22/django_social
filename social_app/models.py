from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    time_made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name

    class Meta:
        ordering = ['-time_made']


class Like(models.Model):
    username = models.CharField(max_length=30)


class Topic(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    teams = models.ManyToManyField(Team)
    likes = models.ManyToManyField(Like)

    class Meta:
        ordering = ['-time_created']


class UserProfile(models.Model):
    user = models.OneToOneField(User)


@receiver(post_save, sender="auth.User")
def user_profile_create(sender, **kwargs):
   created = kwargs.get("created")
   if created:
       instance = kwargs.get("instance")
       UserProfile.objects.create(user=instance)
