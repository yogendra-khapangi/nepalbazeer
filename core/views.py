from django.shortcuts import render,HttpResponse
from math import ceil
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    n=len(products)
    nSlide=n//4+ceil((n//4)-(n//4))
    params={'product':products,'no_of_slide':nSlide,'range':range(1,nSlide)}
    return render(request,"core/index.html",params)



def about(request):
    return render(request,"core/about.html")

def contact(request):
    return render(request,"core/contact.html")

def traker(request):
    return render(request,"core/traker.html")

def search(request):
    return render(request,"core/search.html")

def productview(request):
    return render(request,"core/productview.html")

def checkout(request):
    return render(request,"core/checkout.html")


