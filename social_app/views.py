from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView

from social_app.models import UserProfile, Topic, Team


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class NewUserCreationForm(UserCreationForm):
    age = forms.IntegerField()


class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreationForm

    def form_valid(self, form):
        user_object = form.save()
        user_age = form.cleaned_data.get("age")
        UserProfile.objects.create(user=user_object, age=user_age)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("login")


class TopicCreateView(CreateView):
    model = Topic
    fields = ('title', 'body', 'teams')

    def form_valid(self, form):
        topic_object = form.save(commit=False)
        topic_object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("topic_list")


class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic


class TeamCreateView(CreateView):
    model = Team
    fields = ('team_name',)

    def get_success_url(self):
        return reverse("topic")

class TeamListView(ListView):
    model = Team

class UserDetailView(DetailView):
    model = User

class TeamDetailView(DetailView):
    model = Team