from django.shortcuts import render,HttpResponse
from math import ceil
from .models import Contact, Product


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # n=len(products)
    # nSlide=n//4+ceil((n//4)-(n//4))
    # params={'product':products,'no_of_slide':nSlide,'range':range(1,nSlide)}
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n /4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
    return render(request,"core/index.html",params)



def about(request):
    return render(request,"core/about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,"core/contact.html")

def traker(request):
    return render(request,"core/traker.html")

def search(request):
    return render(request,"core/search.html")

def productview(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,"core/productview.html",{"product":product[0]})

def checkout(request):
    return render(request,"core/checkout.html")


