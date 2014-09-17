from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^bits/', include('bitbilder.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('bitbilder.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
