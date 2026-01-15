from django.db import models

# Create your models here.
class Kitob(models.Model):
    nomi = models.CharField(max_length=200)
    muallif = models.CharField(max_length=100)
    nashr_yili = models.IntegerField()
    kitob_turi = models.CharField(max_length=100, default='Noma\'lum')
    kitob_linki = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.nomi
