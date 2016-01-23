"""blog URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles.views import HelloTemplate
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^admin/',include(admin.site.urls)),
	url(r'^articles/',include('articles.urls')),
	url(r'^hello/$','articles.views.hello'),
	url(r'^hello_template/$','articles.views.hello_template'),
	url(r'^hello_template_simple/$','articles.views.hello_template_simple'),
	url(r'^hello_class_view/$',HelloTemplate.as_view()),
	
	
	url(r'^accounts/login/$', 'blog.views.login'),
    url(r'^accounts/auth/$', 'blog.views.auth_view'),
    url(r'^accounts/logout/$', 'blog.views.logout'),
    url(r'^accounts/loggedin/$', 'blog.views.loggedin'),
    url(r'^accounts/invalid/$', 'blog.views.invalid_login'),
    url(r'^accounts/register/$', 'blog.views.register_user'),
    url(r'^accounts/register_success/$', 'blog.views.register_success'),
    url(r'^accounts/contactus/$', 'blog.views.contactus'),
    url(r'^accounts/repeat_login/$', 'blog.views.repeat_login'),
    url(r'^accounts/repeat_logout/$', 'blog.views.repeat_logout'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
