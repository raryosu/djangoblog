from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raryog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^entries/', include('entries.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
