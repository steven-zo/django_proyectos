from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return render(request, 'hola/index.html')

def hola2(request):
    return HttpResponse('hola 2')

def saludo(request, nombre):
    #pasar variables a  la vista
    context = {'nombre' : nombre}
    return render(request, 'hola/saludo.html', context)

def moneda(request):
    num = 1
    context = {'num':num}
    return render(request, 'hola/mondeda.html', context)