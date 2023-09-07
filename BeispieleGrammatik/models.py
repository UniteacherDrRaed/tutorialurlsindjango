from django.db import models

# Create your models here.
class BeispielFuerArtikel(models.Model):
    Artikel=models.CharField(max_length=10)
    Typ=models.CharField(max_length=20)
    Beispiel=models.CharField(max_length=200)
      
    def __str__(self):
        return f"Artikel: {self.Artikel} Typ: {self.Typ} Beispiel: {self.Beispiel}"
     