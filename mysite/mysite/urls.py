from django.conf.urls import import include, url
from django.contrib import import admin

urlpatterns = [
        url(r'^polls/', include('polls.urls')),
        url(r'^admin/', admin.site.urls),
]
