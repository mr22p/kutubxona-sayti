from django.urls import path
from . import views

urlpatterns = [
    path('narxlar/', views.narxlar_page, name='narxlar'),
    path('', views.narxlar_page, name='home'),
]