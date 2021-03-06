"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import homepage.views
import blog.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage$', homepage.views.homepage, name='homepage'),
    url(r'^about$', homepage.views.about, name='about'),
    url(r'^$', homepage.views.as_view(), name='index'),
    url(r'^contact$', homepage.views.contact, name='contact'),
    url(r'^blog/(\S+)/(\S+)/$', blog.views.blog_post),
    url(r'^blog/(\S+)/$', blog.views.blog_index),
    url(r'^poll$', homepage.views.poll, name='poll'),
    url(r'^(?P<pk>[0-9]+)/$', homepage.views.as_view(), name='detail'),#tuitorial
    url(r'^(?P<pk>[0-9]+)/results/$', homepage.views.as_view(), name='results'),#tuitorial
    url(r'^(?P<question_id>[0-9]+)/vote/$', homepage.views.vote, name='vote'),#tuitorial
]
