from django.shortcuts import render, redirect, get_object_or_404 # Hammasi shu yerda bo'lishi shart
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Kitob
from decouple import config

def narxlar_page(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'narxlar.html', {'kitoblar': kitoblar})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def sevimli(request):
    return render(request, 'sevimli.html')

def kitoblar(request):
    return render(request, 'kitoblar.html')

def sozlamalar(request):
    return render(request, 'sozlamalar.html')

def kabinet_view(request):
   
    return render(request, 'kabinet.html')

def logout_view(request):
    
    return redirect('home')

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"  

class FavoritPageView(ListView):
    model = Kitob
    template_name = "favorit.html"    

    def get_queryset(self):
        return Kitob.objects.filter(is_favorite=True)

def kitblist(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'kitob.html', {'kitoblar': kitoblar})

def yurakcha(request, yurak_id):
    try:
        # get_object_or_404 endi ishlaydi
        tanlangan_yurak = get_object_or_404(
            Kitob,
            pk=request.POST.get("yurakcha") # .get ishlatish xavfsizroq
        )
    except (Kitob.DoesNotExist, KeyError):
        raise Http404("Yurakcha bilan nimadir xatolik ketti...")
    else:
        tanlangan_yurak.is_favorite = not tanlangan_yurak.is_favorite
        tanlangan_yurak.save()
        return HttpResponseRedirect(reverse("kitoblar"))

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pas = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu foydalanuvchi nomi allaqachon band!')
            return render(request, 'register.html')

        if not pas or len(pas) < 4:
            messages.error(request, 'Parol juda qisqa! Kamida 4 ta belgi bo‘lishi kerak.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, password=pas)
        user.save()

        messages.success(request, 'Muvaffaqiyatli ro‘yxatdan o‘tdingiz!')
        return redirect('sozlamalar')

    return render(request, 'register.html')