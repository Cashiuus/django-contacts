from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('contacts.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    ]