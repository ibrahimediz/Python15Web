from django.urls import path
from . import views
urlpatterns = [
    path('', views.kayitlist, name='kayit_list'),
    path('kayit/<int:pk>/',views.kayitdetay,name="kayitagit"),
    path('kayit/yeni',views.yenikayit,name="kayityeni"),
    path('kayit/duzenle/<int:pk>',views.kayit_duzenle,name="kayitduzenle"),
]

