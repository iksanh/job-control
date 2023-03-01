from django.db import models

# Create your models here.



class CategoryJabatan(models.Model):
    class Meta:
        db_table = 'employee_kategory_jabatan'
    kategory = models.CharField(max_length=150)


class Jabatan(models.Model):
    kategori_jabatan = models.ForeignKey(CategoryJabatan, on_delete=models.CASCADE)
    nama_jabatan = models.CharField(max_length=200)


class Pegawai(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=200)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    # pangakat = models.ForeignKey(PangkatGolongan, on_delete=models.CASCADE)

class PangkatGolongan(models.Model):
    class Meta:
        db_table = 'employee_pangkat_golongan'
    nama_pangkat = models.CharField(max_length=50)
    golongan = models.CharField(max_length=10)
    ruang = models.CharField(max_length=2)

