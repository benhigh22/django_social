from django.contrib import admin

from social_app.models import UserProfile, Topic, Team

admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Team)