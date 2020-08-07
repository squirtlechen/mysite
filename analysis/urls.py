from django.urls import path
from .views import table_view, AnalysisView


app_name = 'analysis'
urlpatterns = [
    path('', AnalysisView.as_view(), name='all'),
    path('table', table_view, name='table')
]