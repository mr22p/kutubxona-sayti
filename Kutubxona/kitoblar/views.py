from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import reverse

from .models import Kitob

def narxlar_page(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'narxlar.html', {'kitoblar': kitoblar})


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"  

class FavoritPageView(ListView):
    model = Kitob
    template_name = "favorit.html"


    # bu funksiya is_favorite ustunning True 
    # qiymaga ega bo'lgan qatorni qaytaradi.
    def get_queryset(self):
        return Kitob.objects.filter(is_favorite=True)
    

class KitobListView(ListView):
    model = Kitob
    template_name = "kitob.html"


# Bu yurakchani ustiga bosilganda htmldan 
# keladigan post ni olib yurakchani to'ldiradi yoki to'ldirmaydi
def yurakcha(request, yurak_id):
    try:
        tanlangan_yurak = get_object_or_404(
            Kitob,
            pk=request.POST["yurakcha"]
            )

    except Kitob.DoesNotExist:
        raise Http404("Yurakcha bilan nimadir xatolik ketti...")
    else:
        if tanlangan_yurak.is_favorite:
            tanlangan_yurak.is_favorite = False
        else:
            tanlangan_yurak.is_favorite = True

        tanlangan_yurak.save()

        return HttpResponseRedirect(reverse("kitoblar"))
    
