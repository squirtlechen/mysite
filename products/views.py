from django.shortcuts import render
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def product_create_view_pure(request):
    try:
        print(request,request.method)
        my_form = RawProductForm()
        if request.method == "POST":
            my_form = RawProductForm(request.POST)
            if my_form.is_valid():
                print(my_form.cleaned_data)
            else:
                print(my_form.errors)
        context={
            'form':my_form
            }
            
        return render(request, "products_create_pureform.html", context)
    except:
        print("Get some error")

def product_create_view_html(request):
    print("GET:",request.GET)
    print("POST:",request.POST)
    #my_new_title = request.POS.get('title')
    # Product.objects.create(title=my_new_title)
    context={}
    return render(request, "products_create_html.html", context)

def product_create_view_django(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
       form.save()
       form = ProductForm()

    context={
        'form':form
    }
    return render(request, "products_create_django.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context={
        "object":obj
    }

    return render(request, "products.html", context)