from employee.models import PangkatGolongan
from satker.models import SatuanKerja, UnitKerja, SatuanUnitKerja
from .serilializers import PangkatGolonganSerializers, SatuanKerjaSerializer, UnitKerjaSerializer, SatuanUnitKerjaSerializer
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
"""
Api for Satuan Kerja Using class based view
"""


class SatuanUnitKerjaList(APIView):
    def get(self, request, format = None):
        satuan_unit_kerja = SatuanUnitKerja.objects.all()
        serializer = SatuanUnitKerjaSerializer(satuan_unit_kerja, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        id_get = SatuanKerja(id = request.data.get('satuan_kerja'))
        unit_satker_get = request.data.get('unit_satker')
        unit_kerja = []
        for i in unit_satker_get:
            unit_kerja.append(UnitKerja(id=i))

        for uk in unit_kerja:
            simpan = SatuanUnitKerja(satuan_kerja=id_get, unit_kerja=uk)
            simpan.save()


        return Response({'message' : f'{len(unit_kerja)} Kerja  berhasil disimpan di  Satuan Kerja {id_get.nama} '})

    

class SatuanKerjaList(APIView):
    #get method 
    def get(self, request, format = None):
        satker = SatuanKerja.objects.all()
        serializer = SatuanKerjaSerializer(satker, many=True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = SatuanKerjaSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class SatuanKerjaDetail(APIView):
    #get object
    def get_object(self, pk):
        try:
            return SatuanKerja.objects.get(pk =  pk)
        except SatuanKerja.DoesNotExist:
            raise Http404    

    #api get
    def get(self, request, pk , format=None):
        satker_detail  = self.get_object(pk)
        serializer = SatuanKerjaSerializer(satker_detail)
        return Response(serializer.data)
    
    #api put
    def put(self, request, pk, format = None):
        satker_detail = self.get_object(pk)
        serializer = SatuanKerjaSerializer(satker_detail, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    #api delete
    def delete(self, request, pk , format = None):
        satker_detail = self.get_object(pk)
        print(satker_detail)
        satker_detail.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
        
# class Satuan
"""
Using generic class-based views
"""

class UnitKerjaList(generics.ListCreateAPIView):
    queryset = UnitKerja.objects.all()
    serializer_class = UnitKerjaSerializer

class UnitKerjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitKerja.objects.all()
    serializer_class = UnitKerjaSerializer
    

#. Pangkat Golongan
#. function base view
@csrf_exempt
def pangkat_golongan(request):
    if request.method == 'GET':
        pangkat_golongan = PangkatGolongan.objects.all()
        serializer = PangkatGolonganSerializers(pangkat_golongan, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif  request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PangkatGolonganSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status = 400)
    

@csrf_exempt
def pangkat_golongan_detail(request, pk):
    try:
        pangkat_golongan = PangkatGolongan.objects.get(pk = pk)
    except:
        return HttpResponse(status= 404)
    
    if request.method == 'GET':
        serializer = PangkatGolonganSerializers(pangkat_golongan)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PangkatGolonganSerializers(pangkat_golongan, data = data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message' : 'Success update data ', 'data' : serializer.data })
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        if pangkat_golongan.delete() : 
            return JsonResponse({'message':  'Success Delete Data'})
        else:
            JsonResponse({'message':  'Gagal Delete Data'})