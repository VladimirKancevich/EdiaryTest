from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('', include('app1.urls')),
    path('admin/', admin.site.urls),
    # path('account/', include('account.urls')),
]
