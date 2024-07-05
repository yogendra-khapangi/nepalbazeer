from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"core/index.html")

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


