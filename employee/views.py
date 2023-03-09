from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import Pegawai, PangkatGolongan
from jabatan.models import  CategoryJabatan, Jabatan
from satker.models import SatuanKerja, UnitKerja
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.

"""
def list_pegawai(request):
    pegawai = Pegawai.objects.all()
    context  = {'pegawai' : pegawai, 
                'title' : 'Daftar Pegawai'}
    
    return render(request, 'employee/list_employee.html', context)

def create_pegawai(request):
    pass
    
def edit_pegawai(request):
    pass

def delete_pegawai(request):
    pass

def detail_pegawai(request):
    pass

"""