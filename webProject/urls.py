
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
]
