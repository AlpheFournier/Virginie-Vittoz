
from django.conf.urls import url
from django.contrib import admin
from virginieSite.views import index, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name = 'index'),
    url(r'^contact/', contact, name=contact)
]
