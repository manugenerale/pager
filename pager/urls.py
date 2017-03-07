# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from views import PageDetailView

urlpatterns = [ 
    url(r'^(?P<slug>[-\w]+)/$', PageDetailView.as_view(), name='page-detail'),
]
