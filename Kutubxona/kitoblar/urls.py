from django.urls import path
from .views import HomePageView, AboutPageView, FavoritPageView, KitobListView

urlpatterns = [ 
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('favorit/', FavoritPageView.as_view(), name='favorit'),
    path('kitoblar/', KitobListView.as_view(), name='kitoblar'),
]