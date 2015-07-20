from django.conf.urls import url
from lists import views

urlpatterns = [
    # Examples:
    url(r'^new$', views.new_list, name='new_list'),
    url(r'(\d+)/$', views.view_list, name='view_list'),
    
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
]
