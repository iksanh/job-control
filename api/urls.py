from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('pangkat-golongan', views.pangkat_golongan, name = 'api-pangkat-golongan'),
    path('pangkat-golongan/<int:pk>', views.pangkat_golongan_detail, name = 'api-detail-pangkat-golongan'),

    path('satuan-kerja',  views.SatuanKerjaList.as_view()),
    path('satuan-kerja/<int:pk>',  views.SatuanKerjaDetail.as_view()),


    path('unit-kerja',  views.UnitKerjaList.as_view()),
    path('unit-kerja/<int:pk>',  views.UnitKerjaDetail.as_view()),


    path('unit-satuan-kerja',  views.SatuanUnitKerjaList.as_view()),
    # path('unit-kerja/<int:pk>',  views.UnitKerjaDetail.as_view())
    

]

urlpatterns = format_suffix_patterns(urlpatterns)