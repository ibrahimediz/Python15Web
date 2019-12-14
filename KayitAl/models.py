from django.db import models
from django.utils import timezone

class KayitModels(models.Model):
    adi = models.CharField(max_length=60)
    soyadi = models.CharField(max_length=60)
    cinsiyetCh = [(0,"ERKEK"),(1,"KADIN")]
    cinsiyet = models.CharField(max_length=15,choices=cinsiyetCh)
    tcKimlikNo = models.BigIntegerField()
    kayit_zaman = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.adi+"-"+self.soyadi

