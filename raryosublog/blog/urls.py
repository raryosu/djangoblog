from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.show, name='show'),
        url(r'^edit/$', views.edit, name='edit'),
)
