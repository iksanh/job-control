from django.db import models

#unit kerja
class UnitKerja(models.Model):
    class Meta:
        db_table = 'employee_unit_kerja'
    nama = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nama

class SatuanKerja(models.Model):
    class Meta:
        db_table = 'employee_satuan_kerja'
        
    nama = models.CharField(max_length=150)
    unit_satker = models.ManyToManyField(UnitKerja, through='SatuanUnitKerja')


    

class SatuanUnitKerja(models.Model):
    list_dislpay = ['satuan ', 'unit']
    class Meta:
        db_table = 'employee_satuan_unit_kerja'
    satuan_kerja = models.ForeignKey(SatuanKerja, on_delete=models.CASCADE, null=True)
    unit_kerja = models.ForeignKey(UnitKerja, on_delete=models.CASCADE, null = True) 

    # def satuan(self, obj):
    #     return self.satuan_kerja.nama
    # def unit(self, obj):
    #     return self.unit_kerja.nama




