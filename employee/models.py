from django.db import models
from satker.models import SatuanKerja, SatuanUnitKerja
from jabatan.models import StatusJabatan, Jabatan

# Create your models here.
class PangkatGolongan(models.Model):
    class Meta:
        db_table = 'employee_pangkat_golongan'
    nama_pangkat = models.CharField(max_length=50)
    golongan = models.CharField(max_length=10)
    ruang = models.CharField(max_length=2)


class Pegawai(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=200)
    jabatan = models.ManyToManyField(Jabatan, related_name='jabatan_pegawai', through='PegawaiJabatan')
    tipe_jabatan = models.ManyToManyField(StatusJabatan, related_name='jabatan_pegawai', through='PegawaiJabatan')
    satuan_kerja = models.ManyToManyField(SatuanUnitKerja, through='PegawaiJabatan')
    pangkat = models.ForeignKey(PangkatGolongan, on_delete=models.CASCADE, null=True)

class PegawaiJabatan(models.Model):
    class Meta:
        db_table = 'employee_pegawai_jabatan'
    
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, null=True)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(StatusJabatan, on_delete=models.CASCADE, null=True)
    satuan_kerja = models.ForeignKey(SatuanUnitKerja, on_delete=models.CASCADE, null=True)



