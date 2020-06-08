from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    context={

    }
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    my_context={
        "name":"Yi-Fan Chen",
        "number": 123,
        "my_list":[12,34,56,97]
    }
    return render(request, "about.html", my_context)
