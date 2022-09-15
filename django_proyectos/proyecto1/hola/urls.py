from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name='hola'),
    path('hola2/', views.hola2, name='hola2'),
    #para aceptar variables en el link
    #path('<str:nombre>/',views.saludo, name='saludo'),
    path('moneda/', views.moneda, name='moneda')
]
