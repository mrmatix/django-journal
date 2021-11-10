# defines RL patterns for learning_logs

from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views

app_name = "users"
urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),

    # shows all topics
    url(r'^topics/$', views.topics, name='topics'),

    # detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # page for adding na new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
