from django.urls import path
from .views import HomePageView, KitobPageView


urlpatterns = [
    path("kitob/", KitobPageView.as_view(), name="kitob"),
    path("", HomePageView.as_view(), name="base")
]