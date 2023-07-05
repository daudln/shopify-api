from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("store.urls")),
    path("playground/", include("playground.urls")),
    # path("silk/", include("silk.urls", namespace="silk")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
