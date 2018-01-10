"""Defines url patterns for learning logs."""

from django.conf.urls import url
from learning_logs import views

app_name = 'learning_logs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    # In Django 2, you'd do this:
    # django.url.path('topics/<int:topic_id>/', views.topic, name='topic'),
    # But in Django 1.11, we do this:
    url(r'^topics/(\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]
