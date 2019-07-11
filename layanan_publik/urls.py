from django.urls import path,re_path
from . import views

app_name='layanan_publik'
urlpatterns=[
    path('',views.index,name='index'),

    # Administrasi Index
    path('administrasi/',views.administrasiIndex,name='administrasi'),

    # Administrasi Kependudukan URL
    path('administrasi/ktp',views.administrasiKTP,name='administrasiKTP'),


    # Perizinan Index
    path('perizinan/',views.perizinanIndex,name='perizinanIndex'),

    # Permohonan Usaha URL
    path('permohonan-usaha/',views.permohonanUsaha,name='permohonanUsaha'),
    # Perizinan Acara URL
    path('perizinan-acara/',views.perizinanAcara,name='perizinanAcara'),
]