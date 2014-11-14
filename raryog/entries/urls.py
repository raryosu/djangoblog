from django.conf.urls import patterns, url, include
from entries.models import Entry

info_dict = {
    'queryset':Entry.objects.all(),
    }

urlpatterns = patterns('',
                       (r'^$',
                        'django.views.generic.list_detail.object_list',
                        info_dict),
                       )

