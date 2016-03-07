from django.contrib import admin

from social_app.models import UserProfile, Topic, Teammate

admin.site.register(UserProfile)
admin.site.register(Teammate)
admin.site.register(Topic)
