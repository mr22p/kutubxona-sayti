from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Kitob


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"  

class FavoritPageView(TemplateView):
    template_name = "favorit.html"   

class KitobListView(ListView):
    model = Kitob
    template_name = "kitob.html"
    
def narxlar_page(request):
    kitoblar = Kitob.objects.all() 
    # 'prices.html' o'rniga 'narxlar.html' deb yozing
    return render(request, 'narxlar.html', {'kitoblar': kitoblar})