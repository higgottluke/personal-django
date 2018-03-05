from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^sun/$', views.sun, name='sun'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.blog_home, name='blog'),
	url(r'^blog/([a-zA-Z0-9-\']*)/$', views.blog_post, name='blog_post'),
	url(r'^blog/tag/([a-zA-Z0-9-\']*)/$', views.blog_home, name='blog_by_tag'),
	url(r'^projects/$', views.projects_home, name='projects_list'),
	url(r'^rateyaboss/$', views.rateyaboss, name="CPSC 473 Dummy"),
	url(r'^projects/([a-zA-Z0-9-\']*)/$', views.project, name='project'),
	url(r'^projects/tag/([a-zA-Z0-9-\']*)/$', views.projects_home, name='projects_by_tag'),
	url(r'^contact/$', views.contact, name='contact')
]
