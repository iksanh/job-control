from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create/', views.create_job , name='job-create'),
    path('edit/<int:id>/', views.edit_job , name='job-edit'),
    path('delete/<int:id>/', views.delete_job , name='job-delete'),
    path('about/', views.about , name='about')
]
