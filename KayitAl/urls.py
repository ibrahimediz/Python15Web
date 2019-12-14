from django.urls import path
from . import views
urlpatterns = [
    path('', views.kayitlist, name='kayit_list'),
]