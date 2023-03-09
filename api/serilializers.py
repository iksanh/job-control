from django.db.models import fields
from rest_framework import serializers
from satker.models import SatuanKerja, UnitKerja, SatuanUnitKerja
from jabatan.models import Jabatan, StatusJabatan, CategoryJabatan
from employee.models import  PangkatGolongan #Pegawai,


# class PegawaiSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Pegawai
#         fields = '__all__'

class PangkatGolonganSerializers(serializers.ModelSerializer):
    class Meta:
        model = PangkatGolongan
        fields = '__all__'

class UnitKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitKerja
        fields = '__all__'

class SatuanKerjaSerializer(serializers.ModelSerializer):
    unit_satker = UnitKerjaSerializer(many = True, read_only = True)
    class Meta:
        model = SatuanKerja
        fields = ('nama', 'unit_satker')

class SatuanUnitKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatuanUnitKerja
        fields = '__all__'

class CategoryJabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryJabatan
        fields = '__all__'

class JabatanSerializer(serializers.ModelSerializer):
    kategori_jabatan = CategoryJabatanSerializer(many=True, read_only=True)
    class Meta:
        model = Jabatan
        fields = ('nama_jabatan', 'kategory_jabatan')

class StatusJabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusJabatan
        fields = '__all__'