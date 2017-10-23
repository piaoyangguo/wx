"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from chanping.views import index, welcome, newpage

urlpatterns = [
    url(r'^devadmin/', include(admin.site.urls)),
    url(r'^(?P<pwd>\w+)/index/$', index, name="index"),
    url(r'^$', welcome),
    url(r'^newpage/$', newpage, name="newpage"),
]
