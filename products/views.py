from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.
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