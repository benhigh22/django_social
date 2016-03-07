from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView

from social_app.models import UserProfile, Topic, Teammate


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class NewUserCreationForm(UserCreationForm):
    age = forms.IntegerField()
    favorite_team = forms.CharField(max_length=50)
    years_of_experience = forms.IntegerField()


class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreationForm

    def form_valid(self, form):
        user_object = form.save()
        user_age = form.cleaned_data.get("age")
        user_fav_team = form.cleaned_data.get("favorite_team")
        user_years_exp = form.cleaned_data.get("years_of_experience")
        UserProfile.objects.create(user=user_object, age=user_age,
                                   favorite_team=user_fav_team, years_of_experience=user_years_exp)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("login")


class TopicCreateView(CreateView):
    model = Topic
    fields = ('message_post',)

    def form_valid(self, form):
        topic_object = form.save(commit=False)
        topic_object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("topic_list")


class TopicListView(ListView):
    model = Topic


class TeammateCreateView(CreateView):
    model = Teammate
    fields = ('user','relationships')
