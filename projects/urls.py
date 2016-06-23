from django.conf.urls import url

from . import views

app_name = 'projects'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<hackathon>[0-9]+)/$', views.index, name='index'),
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.project, name='project'),
    url(r'^add/$', views.add_project, name='add_project'),
    url(r'^edit/(?P<project_id>[0-9]+)/$', views.edit_project, name='edit_project')
]