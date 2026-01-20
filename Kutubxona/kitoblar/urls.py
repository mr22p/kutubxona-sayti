from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('favorit/', views.FavoritPageView.as_view(), name='favorit'),
    path('kitoblar/', views.KitobListView.as_view(), name='kitoblar'),
    path('narxlar/', views.narxlar_page, name='narxlar'),
    path('', views.HomePageView.as_view(), name='home'), # Agar HomePageView klassingiz bo'lsa
]