from django.db import models

# Create your models here.

#struktural fungsional pelaksana
class CategoryJabatan(models.Model):
    class Meta:
        db_table = 'kategory_jabatan'
    kategory = models.CharField(max_length=150)


class Jabatan(models.Model):
    class Meta:
        db_table = 'jabatan'
    kategori_jabatan = models.OneToOneField(CategoryJabatan, on_delete=models.CASCADE, null= True)
    nama_jabatan = models.CharField(max_length=200)

#plt, plh, definitif
class StatusJabatan(models.Model):
    class Meta:
        db_table = 'status_jabatan'
    nama_type = models.CharField(max_length=25)
