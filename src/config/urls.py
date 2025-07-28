from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.public.urls', namespace='public')),
    path('contactus/', include('apps.contactus.urls', namespace='contactus')),

    path('rosetta/', include('rosetta.urls')),
    path('captcha/', include("captcha.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
