from django.db import models

class Kitob(models.Model):
    nomi = models.CharField(max_length=200)
    muallif = models.CharField(max_length=100)
    nashr_yili = models.IntegerField()
    kitob_turi = models.CharField(max_length=100, default='Noma\'lum')
    kitob_linki = models.TextField(max_length=200, blank=True)
    # Narx maydonini mana bu yerga qo'shing:
    narxi = models.IntegerField(default=0, verbose_name="Kitob narxi")

    def __str__(self):
        return self.nomi
    

    