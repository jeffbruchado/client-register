from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('src.v1.user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
