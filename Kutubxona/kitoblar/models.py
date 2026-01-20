from django.db import models

class Kitob(models.Model):
    nomi = models.CharField(max_length=200)
    muallif = models.CharField(max_length=100)
    nashr_yili = models.IntegerField()
    kitob_turi = models.CharField(max_length=100, default='Noma\'lum')
    kitob_linki = models.TextField(max_length=200, blank=True)
    file = models.FileField(upload_to='static/files', blank=True, null=True)
    image = models.ImageField(upload_to='kitoblar', blank=True, null=True)
<<<<<<< HEAD
    narxi = models.IntegerField()
    def __str__(self):
        return self.nomi
 
=======
    kitob_narxi = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    def __str__(self):
        return self.nomi
    

    
>>>>>>> main
