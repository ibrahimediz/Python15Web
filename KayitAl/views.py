from django.shortcuts import render,redirect,get_object_or_404
from .models import KayitModels

from .forms import KayitForm


def kayitlist(request):
    kayitlar = KayitModels.objects.all()
    return render(request,'kayit/liste.html',{"kayitlar":kayitlar})


def kayitdetay(request,pk):
    kayit = KayitModels.objects.get(pk=pk)
    return render(request,'kayit/detay.html',{"kayit":kayit})


def yenikayit(request):
    if request.method == "POST":
        form = KayitForm(request.POST)
        if form.is_valid():
            kayit = form.save(commit=False)
            kayit.save()
            return redirect('kayitagit', pk=kayit.pk)
    else:
        form = KayitForm()
    return render(request, 'kayit/kayit_edit.html', {'form': form})


def kayit_duzenle(request, pk):
    kayit = get_object_or_404(KayitModels, pk=pk)
    if request.method == "POST":
        form = KayitForm(request.POST, instance=kayit)
        if form.is_valid():
            kayit = form.save(commit=False)
            kayit.save()
            return redirect('kayitagit', pk=kayit.pk)
    else:
        form = KayitForm(instance=kayit)
    return render(request, 'kayit/kayit_edit.html', {'form': form})