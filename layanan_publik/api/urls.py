from django.urls import path,re_path
from . import views

app_name='layanan_publik_api'
urlpatterns=[

    # Permohonan Izin Usaha API URL
    path('list/',views.PermohonanUsahaList.as_view(),name='list-api'),
    re_path(r'^detail/(?P<nama_pemohon>.+)/$',views.PermohonanUsahaDetail.as_view(),name='detail-api'),
    re_path(r'^delete/(?P<id_pemohon>.+)/$',views.PermohonanUsahaDetailDelete.as_view(),name='delete-api'),

    # Administrasi KTP API URL
    path('ktp/list/',views.AdministrasiKTPListAPI.as_view(),name='ktp-list-api'),

    # Permohonan Izin Acara API URL
    path('perizinan-acara/list/',views.PerizinanAcaraListAPI.as_view(),name='perizinan-acara-api-list'),
    path('perizinan-acara/list/post/',views.PerizinanAcaraListAPI.as_view(),name='perizinan-acara-api-post')
]