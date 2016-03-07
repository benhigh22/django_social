from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    favorite_team = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()


class Topic(models.Model):
    message_post = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-time_created']


class Teammate(models.Model):
    user = models.ForeignKey(User)
    relationships = models.ManyToManyField("self", through='Relationship', symmetrical=False, related_name='related_to')


RELATIONSHIP_TEAMMATE = 1
RELATIONSHIP_OPPONENT = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_TEAMMATE, 'Following'),
    (RELATIONSHIP_OPPONENT, 'Blocked'),
)


class Relationship(models.Model):
    from_teammate = models.ForeignKey(Teammate, related_name='from_teammate')
    to_teammate = models.ForeignKey(Teammate, related_name='to_teammate')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)