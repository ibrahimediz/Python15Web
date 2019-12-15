from django.shortcuts import render
from .models import KayitModels


def kayitlist(request):
    kayitlar = KayitModels.objects.all()
    return render(request,'kayit/liste.html',{"kayitlar":kayitlar})