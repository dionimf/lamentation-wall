from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from index_board import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'lamentation_wall.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r"^accounts/profile/*", views.login),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^me/', RedirectView.as_view(url='/lamentacoes')),
                       url(r'^lamentacoes/', RedirectView.as_view(url='/')),
                       url(r'list-counsels', views.list_counsels),
                       url(r'^test$', views.test),
                       url(r'^logout/$', views.logout),
                       #url(r'^/$', include('index_board.urls')),
                       url(r'^auth/$', views.auth_complete),
                       url(r'^auth/google$', views.google_auth_complete),
                       url(r'^auth/twitter$', views.twitter_auth_complete),
                       url(r'crytogether', views.cry_together),
                       url(r'save-counsel', views.save_counsel),
                       url(r'^google-login$', views.google_login),
                       url(r'auth/', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^$', views.index),
)
