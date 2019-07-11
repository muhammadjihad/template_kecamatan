from rest_framework.views import APIView
from layanan_publik.models import (
    PermohonanUsaha,
    AdministrasiKTP,
    PerizinanAcara
)
from rest_framework.response import Response
from .serializers import PermohonanUsahaListSerializer
from rest_framework import mixins
from rest_framework import generics
import datetime

# Permohonan Usaha API
class PermohonanUsahaList(generics.ListCreateAPIView):

    def get(self,request,format=None):
        allObj=PermohonanUsaha.objects.all()
        obj_list=[]
        for obj in allObj:
            pack={
                'nama_pemohon':obj.nama_pemohon,
                'nomor_induk':obj.nomor_induk,
                'nama_usaha':obj.nama_usaha,
                'deskripsi_usaha':obj.deskripsi_usaha,
                'id':obj.id,
                'verifikasi':obj.verifikasi,
                'foto':obj.foto.url
            }
            obj_list.append(pack)
        content={
            'status':'berhasil',
            'data':obj_list
        }
        return Response(content)

    def post(self,request,format=None):
        PermohonanUsaha.objects.create(
            nama_pemohon=request.data['nama_pemohon'],
            nomor_induk=request.data['nomor_induk'],
            nama_usaha=request.data['nama_usaha'],
            deskripsi_usaha=request.data['deskripsi_usaha']
        )
        return Response(request.data)

class PermohonanUsahaDetail(APIView):

    def get(self,request,*args,**kwargs):
        print(kwargs)
        obj=PermohonanUsaha.objects.get(id=int(kwargs['nama_pemohon']))
        content={
            'nama_pemohon':obj.nama_pemohon,
            'nomor_induk':obj.nomor_induk,
            'nama_usaha':obj.nama_usaha,
            'deskripsi_usaha':obj.deskripsi_usaha
        }
        return Response(content)

class PermohonanUsahaDetailDelete(APIView):

    def post(self,request,*args,**kwargs):
        PermohonanUsaha.objects.get(id=kwargs['id_pemohon']).delete()
        return Response({
            'pesan':'berhasil'
        })


# Administrasi KTP API
class AdministrasiKTPListAPI(APIView):

    def get(self,request,*args,**kwargs):
        obj=AdministrasiKTP.objects.all().values(
            'nama',
            'tempat_lahir',
            'tanggal_lahir',
            'status_perkawinan'
        )
        content={
            'pesan':'berhasil',
            'data':obj
        }
        return Response(content)

    def post(self,request,*args,**kwargs):
        print(request.data)
        date_obj=datetime.datetime.strptime(request.data['tanggal_lahir'],'%Y-%m-%d %H:%M:%S.%f')
        date_obj=date_obj.date()
        AdministrasiKTP.objects.create(
            nama=request.data['nama'],
            tempat_lahir=request.data['kota_lahir'],
            tanggal_lahir=date_obj,
            alamat=request.data['alamat'],
            agama=request.data['agama'],
            status_perkawinan=request.data['status_perkawinan'],
            pekerjaan=request.data['pekerjaan'],
            pilihan_status_wn=request.data['status_warga']
        )
        print("BERHASIL")
        return Response({
            'pesan':'testing123'
        })

# Perizinan Acara API
class PerizinanAcaraListAPI(APIView):

    def get(self,request,*args,**kwargs):
        try:
            if request.query_params['approvekecamatan']:
                acara=PerizinanAcara.objects.filter(approve_kecamatan=True).order_by('-id').values(
                'nama_kegiatan',
                'deskripsi_kegiatan',
                'tanggal_kegiatan',
                'waktu_kegiatan',
                'tempat_kegiatan',
                'nama_ketuapanitia',
                'approve_kecamatan'
            )
        except:
            try:
                if request.query_params['page']:
                    acara=PerizinanAcara.objects.all().order_by('-id').values(
                    'nama_kegiatan',
                    'deskripsi_kegiatan',
                    'tanggal_kegiatan',
                    'waktu_kegiatan',
                    'tempat_kegiatan',
                    'nama_ketuapanitia',
                    'approve_kecamatan'
                    )[:int(request.query_params['page'])]
            except:
                acara=PerizinanAcara.objects.all().order_by('-id').values(
                'nama_kegiatan',
                'deskripsi_kegiatan',
                'tanggal_kegiatan',
                'waktu_kegiatan',
                'tempat_kegiatan',
                'nama_ketuapanitia',
                'approve_kecamatan'
                )

        content={
            'pesan':'berhasil',
            'data':acara
        }
        return Response(content)

    def post(self,request,*args,**kwargs):
        date_obj=datetime.datetime.strptime(request.data['tanggal_kegiatan'],'%Y-%m-%d %H:%M:%S.%f')
        date_obj=date_obj.date()
        time_obj=datetime.time.fromisoformat(request.data['waktu_kegiatan'])
        PerizinanAcara.objects.create(
            nama_kegiatan=request.data['nama_kegiatan'],
            deskripsi_kegiatan=request.data['deskripsi_kegiatan'],
            tanggal_kegiatan=date_obj,
            waktu_kegiatan=time_obj,
            tempat_kegiatan=request.data['tempat_kegiatan'],
            nama_ketuapanitia=request.data['nama_ketuapanitia']

        )
        return Response({
            'pesan':'berhasil'
        })