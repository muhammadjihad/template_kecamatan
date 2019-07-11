from . import models
from django import forms

class PermohonanUsahaForm(forms.ModelForm):
    class Meta:
        model = models.PermohonanUsaha
        exclude=('verifikasi',)
        widgets={
            'nama_pemohon': forms.TextInput(
                attrs={
                    'placeholder':'Masukkan Nama ..'
                }
            ),
            'nomor_induk': forms.TextInput(
                attrs={
                    'placeholder':'Masukkan NIK ..'
                }
            ),
            'nama_usaha':forms.TextInput(
                attrs={
                    'placeholder':'Masukkan nama usaha atau nama perusahaan saudara ...'
                }
            ),
            'deskripsi_usaha':forms.Textarea(
                attrs={
                    'placeholder':'Jelaskan mengenai kegiatan usaha saudara ..',
                    'rows':'3'
                }
            )
        }

class PerizinanAcaraForm(forms.ModelForm):
    class Meta:
        model=models.PerizinanAcara
        exclude=('waktu_pembuatan_laporan','approve_kecamatan')
        widgets={
            'nama_ketuapanitia':forms.TextInput(
                attrs={
                    'placeholder':'Nama Ketua Panitia atau Penanggung Jawab Acara'
                }
            ),
            'alamat':forms.Textarea(
                attrs={
                    'placeholder':'Alamat Rumah Ketua Panitia atau Penanggung Jawab Acara',
                    'rows':'3'
                }
            ),
            'nama_kegiatan':forms.TextInput(
                attrs={
                    'placeholder':'Nama Kegiatan'
                }
            ),
            'deskripsi_kegiatan':forms.Textarea(
                attrs={
                    'placeholder':'Jelaskan kegiatan apa yang akan dilaksanakan',
                    'rows':'4'
                }
            ),
            'tanggal_kegiatan':forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder':'Pilih Tanggal Acara',
                    'type':'date',
                }
            ),
            'waktu_kegiatan':forms.TimeInput(
                attrs={
                    'type':'time'
                }
            ),
            'tempat_kegiatan':forms.TextInput(
                attrs={
                    'placeholder':'Tempat Berlangsungnya Kegiatan'
                }
            )
        }
        labels={
            'nama_ketuapanitia':'Nama Ketua Panitia',
            'waktu_kegiatan':'Waktu Kegiatan (cth : 08:30 PM)'
        }

class AdministrasiKTPForm(forms.ModelForm):
    class Meta:
        model = models.AdministrasiKTP
        exclude=('waktu_pembuatan',)
        widgets={
            'tanggal_lahir':forms.DateTimeInput(
                attrs={
                    'class':'form-control date',
                    'placeholder':'Contoh : 1997-19-05'
                }
            ),
            'nama':forms.TextInput(
                attrs={
                    'placeholder':'Masukkan Nama Lengkap Anda ..'
                }
            ),
            'tempat_lahir':forms.TextInput(
                attrs={
                    'placeholder':'Masukkan Nama Kota Kelahiran Anda ..'
                }
            ),
            'alamat':forms.Textarea(
                attrs={
                    'placeholder':'Masukkan Alamat Anda ..',
                    'rows':'3'
                }
            )
        }
        labels={
            'pilihan_status_wn':'Warga Negara',
            'tanggal_lahir':'Tanggal Lahir - format (tahun-bulan-tanggal)'
        }