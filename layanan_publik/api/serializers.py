from rest_framework import serializers
from layanan_publik.models import PermohonanUsaha

class PermohonanUsahaListSerializer(serializers.ModelSerializer):

    img_url = serializers.SerializerMethodField('foto_url')

    class Meta:
        model=PermohonanUsaha
        fields=(
            'nama_pemohon',
            'nomor_induk',
            'nama_usaha',
            'deskripsi_usaha',
            'verifikasi',
            'id',
            'img_url'
        )

    def foto_url(self,obj):
        return obj.foto.url