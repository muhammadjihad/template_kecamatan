from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('layanan/',include('layanan_publik.urls',namespace='layanan_publik')),

    # API
    path('layanan-api/',include('layanan_publik.api.urls',namespace='layanan_publik_api'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Admin - Kecamatan Sumur Bandung"
admin.site.site_title = "Admin - Kecamatan Sumur Bandung"
admin.site.index_title = "Admin - Kecamatan Sumur Bandung"