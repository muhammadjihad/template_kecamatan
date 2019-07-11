from django.shortcuts import render,redirect
from .forms import (
    PermohonanUsahaForm,
    AdministrasiKTPForm,
    PerizinanAcaraForm
)
from .models import (
    PermohonanUsaha,
    AdministrasiKTP,
    PerizinanAcara
)

# Create your views here.

# Menu Utama
def index(request):
    return render(request,'layanan_publik/index.html')


# <---- Administrasi ----> 

# Menu Utama Layanan Administrasi di Kecamatan
def administrasiIndex(request):
    return render(request,'layanan_publik/administrasi_index.html')

# Layanan Administrasi KTP
def administrasiKTP(request):
    formAdministrasiKTP = AdministrasiKTPForm
    context={
        'form_administrasi_KTP':formAdministrasiKTP,
        'list_orang':AdministrasiKTP.objects.all()
    }
    if request.method == "POST":
        formAdministrasiKTP=AdministrasiKTPForm(request.POST)
        if formAdministrasiKTP.is_valid():
            formAdministrasiKTP.save()
            return redirect('layanan_publik:administrasiKTP')

    return render(request,'layanan_publik/administrasi_ktp.html',context)

# <---- Perizinan ---->

# Perizinan Index
def perizinanIndex(request):
    return render(request,'layanan_publik/perizinan_index.html')

# Permohonan Izin Usaha
def permohonanUsaha(request):
    formPermohonan=PermohonanUsahaForm
    context={
        'form_permohonan_usaha':formPermohonan,
    }
    try:
        print(request.GET['nama_pemohon'])
        context['daftarIzinUsaha']=PermohonanUsaha.objects.filter(nama_pemohon__icontains=request.GET['nama_pemohon']).order_by('-id')
    except:
        context['daftarIzinUsaha']=PermohonanUsaha.objects.all().order_by('-id')
    if request.method == 'POST':
        formPermohonan=PermohonanUsahaForm(request.POST, request.FILES)
        print(request.FILES)
        if formPermohonan.is_valid():
            formPermohonan.save()
            return redirect('layanan_publik:permohonanUsaha')
            
    return render(request,'layanan_publik/permohonan_usaha.html',context)

# Perizinan Acara View
def perizinanAcara(request):
    listAcara=PerizinanAcara.objects.all().order_by('-id').values(
        'nama_kegiatan',
        'waktu_kegiatan',
        'tempat_kegiatan',
        'tanggal_kegiatan',
        'nama_ketuapanitia',
        'approve_kecamatan'
    )
    formPerizinanAcara=PerizinanAcaraForm
    context={
        'form_perizinan_acara':formPerizinanAcara,
        'listAcara':listAcara
    }
    if request.method == 'POST':
        formPerizinanAcara=PerizinanAcaraForm(request.POST)
        if formPerizinanAcara.is_valid():
            formPerizinanAcara.save()
            return redirect('layanan_publik:perizinanAcara')
    return render(request,'layanan_publik/perizinan_acara.html',context)