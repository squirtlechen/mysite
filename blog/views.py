from django.shortcuts import render, get_object_or_404
from .models import Article
from .form import ArticleForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)





def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
       form.save()
       form = ArticleForm()

    context={
        'form':form
    }
    return render(request, "article_create.html", context)
    
