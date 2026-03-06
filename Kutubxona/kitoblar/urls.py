from django.urls import path, include
from . import views  # Barcha views'larni olish uchun
from .views import (
    HomePageView, 
    AboutPageView, 
    FavoritPageView, 
    kitblist,
    yurakcha,
    register, 
    sozlamalar
)

urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('favorit/', FavoritPageView.as_view(), name='favorit'),
    path('kitoblar/', kitblist, name='kitoblar'),
    path('yurakcha/<int:yurak_id>/', yurakcha, name="yurakcha"), 
    path('sozlamalar/', sozlamalar, name='sozlamalar'), 
    
    # Muhim qism: HTMLda 'kabinet' va 'logout' ishlatilgan bo'lsa, 
    # views.py faylingizda shu nomli funksiyalar bo'lishi shart.
    path('kabinet/', views.kabinet_view, name='kabinet'), 
    path('logout/', views.logout_view, name='logout'),
    
    path('accounts/', include('django.contrib.auth.urls')), 
    path('register/', register, name='register'),
]