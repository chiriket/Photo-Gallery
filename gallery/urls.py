from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index, name = 'home'),
    url(r'^image/(\d+)', views.single_image, name = 'single_image'),
    url(r'^location/filtered/$', views.location_filter, name = 'location_filter'),
    url(r'^category/(?P<category>.*)', views.get_category, name = 'category'),
    url(r'^search', views.search, name='search_images')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)