def narxlar_page(request):
    kitoblar = Kitob.objects.all() # Bazadagi barcha kitoblarni olish
    return render(request, 'prices.html', {'kitoblar': kitoblar})