from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('/', admin.site.urls),

    path('api/v1/', include('accounts.urls')),

    path('api/v1/', include('author.urls')),

    path('api/v1/', include('post.urls')),

    path('api/v1/', include('departments.urls')),

    path('api/v1/', include('events.urls')),

    path('api/v1/', include('projects.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
