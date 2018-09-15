# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from core.views import RegisterFormView, Profile

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$', Profile.as_view(), name='profile'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'core/index.html'}, name='logout'),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^$', TemplateView.as_view(template_name='core/index.html'), name='index'),
]
