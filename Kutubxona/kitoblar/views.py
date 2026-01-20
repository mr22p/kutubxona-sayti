from django.shortcuts import render
from .models import Kitob

def narxlar_page(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'narxlar.html', {'kitoblar': kitoblar})


