from django.urls import path
from .views import (
    HomePageView, 
    AboutPageView, 
    FavoritPageView, 
    kitblist,
    yurakcha)

urlpatterns = [ 
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('favorit/', FavoritPageView.as_view(), name='favorit'),
    path('kitoblar/', kitblist, name='kitoblar'),
    path('<int:yurak_id>/yurakcha', yurakcha, name="yurakcha")   #Bu yurakcha funksiyasi ishga tushiradi.  
]