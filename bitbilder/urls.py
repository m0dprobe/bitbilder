from django.conf.urls import patterns, url
from bitbilder import views

urlpatterns = patterns('',
        url(r'^$', views.matrix, name='matrix'),
        url(r'^(?P<bit_id>\d+)/$', views.details, name='details'),
        url(r'^add/$', views.upload, name='upload'),
        url(r'^add/(?P<param>.+)/$', views.upload, name='upload'),
        url(r'^(?P<bit_id>\d+)/claim/$', views.claim, name='claim'),
        url(r'^download/svg/$', views.download_svg_zip, name='download_svg_zip'),
        url(r'^download/images/$', views.download_img_zip, name='download_img_zip'),
        url(r'^download/$', views.download_page, name='download_page')
)
