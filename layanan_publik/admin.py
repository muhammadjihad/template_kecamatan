from django.contrib import admin
from .models import (
    PermohonanUsaha,
    AdministrasiKTP,
    PerizinanAcara
)
# Register your models here.

class PermohonanUsahaAdmin(admin.ModelAdmin):
    list_display=['nama_pemohon','nomor_induk','nama_usaha','deskripsi_usaha','verifikasi']
    list_filter=('verifikasi','nama_pemohon')

class AdministrasiKTPAdmin(admin.ModelAdmin):
    list_display=('nama','tempat_lahir','tanggal_lahir','status_perkawinan')
    list_filter=('status_perkawinan',)


# Registrasi Model Admin Disini
admin.site.register(PermohonanUsaha,PermohonanUsahaAdmin)
admin.site.register(AdministrasiKTP,AdministrasiKTPAdmin)
admin.site.register(PerizinanAcara)