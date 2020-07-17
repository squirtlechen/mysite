from django.urls import path
from .views import ArticleListView, create_article, ArticleDetailView

app_name = 'blog'
urlpatterns = [
    path('<int:id>', ArticleDetailView.as_view(), name='Article'),
    path('', ArticleListView.as_view(), name='Articles'),
    path('create', create_article, name='createbydjango'),

]