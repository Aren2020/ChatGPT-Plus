from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('backend_api.urls')),
    path('admin/', admin.site.urls),
]
