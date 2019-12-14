from django.shortcuts import render


def kayitlist(request):
    return render(request,'kayit/liste.html')