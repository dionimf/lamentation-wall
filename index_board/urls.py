from django.conf.urls import patterns, url

from index_board import views

urlpatterns = patterns('',
                       url(r'crytogether', views.cry_together),
                       url(r'', views.index),)
