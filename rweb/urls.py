from django.contrib import admin
from django.urls import path , include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('allauth.urls')),
    path("research/", include("research.urls")),
    path("ps/", include("ps.urls")),
    
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

"""path("", include("landing.urls")),
    path("am/", include("am.urls")),
    
    path("startup/", include("startup.urls")),
    
    https://sanjaikabilan-curly-waddle-7x6q4rp7v972wqwq-8000.preview.app.github.dev/
    
"""

    
