from django.db import models
# Create your models here.

class PermohonanUsaha(models.Model):

    nama_pemohon=models.CharField(max_length=25)
    nomor_induk=models.IntegerField()
    nama_usaha=models.CharField(max_length=35)
    deskripsi_usaha=models.TextField()
    verifikasi=models.BooleanField(default=False)
    foto=models.ImageField(upload_to='layanan/izin-usaha/foto',default='person.png')

    def __str__(self):
        return self.nama_pemohon

class AdministrasiKTP(models.Model):

    nama = models.CharField(max_length=35)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir=models.DateField()
    alamat=models.TextField()

    PILIHAN_AGAMA=(
        ('Islam','Islam'),
        ('Kristen Katolik','Kristen Katolik'),
        ('Kristen Protestan','Kristen Protestan'),
        ('Budha','Budha'),
        ('Hindu','Hindu'),
        ('Kong Hu Cu','Kong Hu Cu'),
    )
    agama=models.CharField(max_length=17, choices=PILIHAN_AGAMA)

    PILIHAN_STATUS_KAWIN=(
        ('Belum Menikah','Belum Menikah'),
        ('Menikah','Menikah'),
        ('Cerai','Cerai')
    )
    status_perkawinan=models.CharField(max_length=11,choices=PILIHAN_STATUS_KAWIN)
    
    pekerjaan=models.CharField(max_length=45)

    PILIHAN_STATUS_WN=(
        ('WNI','WARGA NEGARA INDONESIA'),
        ('WNA','WARGA NEGARA ASING')
    )   
    pilihan_status_wn=models.CharField(max_length=3,choices=PILIHAN_STATUS_WN)

    waktu_pembuatan=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class PerizinanAcara(models.Model):

    nama_ketuapanitia=models.CharField(max_length=30)
    alamat=models.TextField()
    nama_kegiatan=models.CharField(max_length=55)
    deskripsi_kegiatan=models.TextField()
    tanggal_kegiatan=models.DateField()
    waktu_kegiatan=models.TimeField()
    tempat_kegiatan=models.CharField(max_length=50)

    waktu_pembuatan_laporan=models.DateTimeField(auto_now_add=True)
    approve_kecamatan=models.BooleanField(default=False)

    def __str__(self):
        return self.nama_kegiatan