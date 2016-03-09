from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, UpdateView
from social_app.models import Topic, Team, Like


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm

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


class LikeView(View):

    def get(self, request, pk):
        current_user = User.objects.get(pk=self.request.user.id)
        like_instance = Like.objects.create(username=current_user.username)
        current_topic = Topic.objects.get(pk=pk)
        like_instance.save()
        current_topic.likes.add(like_instance)
        current_topic.save()
        return HttpResponseRedirect("/")