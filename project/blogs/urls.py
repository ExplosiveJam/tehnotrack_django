# coding: utf-8
"""blog URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from blogs.views import *
from django.conf import settings
from comments.views import *


admin.autodiscover()

categories_patterns = [
    url(r'^(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^$', CategoryList.as_view(), name='category_list')
]

blogs_patterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^(?P<pk>\d+)/post$', PostCreate.as_view(), name='post_create'),
    url(r'^(?P<pk>\d+)/edit/$', BlogUpdate.as_view(), name='blog_edit'),
    url(r'^create/$', BlogCreate.as_view(), name='blog_create')
]

posts_patterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdate.as_view(), name='post_edit'),
    url(r'^create/$', PostCreate.as_view(), name='post_create'),
    url(r'^(?P<pk>\d+)/add-comment/$', PostCommentCreate.as_view(), name='add_comment')
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^categories/', include(categories_patterns, namespace='categories')),
    url(r'^blogs/', include(blogs_patterns, namespace='blogs')),
    url(r'^posts/', include(posts_patterns, namespace='posts')),
    url(r'^', include('core.urls', namespace='core'))
]

if settings.DEBUG is True:
    from django.conf.urls.static import static
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
                    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
