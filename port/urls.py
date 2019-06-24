from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url('^projects', views.projects, name = 'projects'),
    url('^contact$', views.contact, name = 'contact'),
    url('^about$', views.about, name = 'about'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
