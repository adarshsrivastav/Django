from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^all/$','articles.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$','articles.views.article'),
	url(r'^language/(?P<language>[a-z\-]+)/$','articles.views.language'),
	#url(r'^create/$', 'articles.views.create'),
	url(r'^like/(?P<article_id>\d+)/$', 'articles.views.like_article'),
	url(r'^search/$','articles.views.search_title'),
	url(r'^login/$', 'blog.views.login'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)