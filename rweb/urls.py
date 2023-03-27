from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('allauth.urls')),
    path("", include("landing.urls")),
    path("research/", include("research.urls", namespace="research")),
    path("am/", include("am.urls", namespace="am")),
    path("ps/", include("ps.urls")),
   # path("playground/", include("playground.urls")),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""
    path("am/", include("am.urls")),
    
    path("startup/", include("startup.urls")),
    
    https://sanjaikabilan-curly-waddle-7x6q4rp7v972wqwq-8000.preview.app.github.dev/
    
"""

    
