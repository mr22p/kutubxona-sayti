from django.db import models

# Create your models here.
class Kitob(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()

    def __str__(self):
        return self.name