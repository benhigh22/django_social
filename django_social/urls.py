"""django_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from social_app.views import UserCreateView, IndexTemplateView, TopicCreateView, TopicListView, TeamCreateView, \
    TopicDetailView, TeamListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexTemplateView.as_view(), name='index'),
    url(r'^signup', UserCreateView.as_view(), name='signup'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout_then_login, name='logout'),
    url(r'^newtopic', TopicCreateView.as_view(), name='topic'),
    url(r'^topiclist', TopicListView.as_view(), name='topic_list'),
    url(r'^newteam', TeamCreateView.as_view(), name='team_create'),
    url(r'^topicdetail/(?P<pk>\d+)', TopicDetailView.as_view(), name='topic_detail'),
    url(r'^teamlist', TeamListView.as_view(), name='team_list'),
]
