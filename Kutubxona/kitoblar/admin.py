from django.contrib import admin
from .models import Kitob
# 2. Faqat mana bu qismini qoldiring va narxni ko'rsatish uchun list_display qo'shing:
@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    # Bu yerda Narxi maydonini kiritganingiz uchun u asosiy ro'yxatda ko'rinadi
    list_display = ('nomi', 'muallif', 'Narxi')
