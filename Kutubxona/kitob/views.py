from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Kitob

# Create your views here.
class HomePageView(TemplateView):
    template_name = "base.html"

class KitobPageView(ListView):
    model = Kitob
    template_name = "kitob.html"

