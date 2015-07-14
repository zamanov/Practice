"""restful URL Configuration

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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from serv.views import CellList, ObjectList


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns(
    'serv.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cells/?$', CellList.as_view()),
    url(r'^objects/?$', ObjectList.as_view()),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    url(r'^cells/(?P<pk>[0-9]+)/?$', 'cell_detail'),
    url(r'^objects/(?P<pk>[0-9]+)/?$', 'object_detail'),
)
