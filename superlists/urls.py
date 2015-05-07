from django.conf.urls import patterns, include, url
from django.contrib import admin
from lists import views

urlpatterns = [
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
]
