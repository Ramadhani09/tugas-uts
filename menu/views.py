from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    home = loader.get_template('home.html')
    return HttpResponse(home.render())

def produk(request):
    produk = loader.get_template('produk.html')
    return HttpResponse(produk.render())

def kategori(request):
    kategori = loader.get_template('kategori.html')
    return HttpResponse(kategori.render())

# def base(request):
#     base = loader.get_template('base.html')
#     return HttpResponse(base.render())e.
