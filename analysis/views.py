from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
import pandas as pd 
from google.cloud import bigquery
from .models import Table

# Create your views here.

def table_view(request, *args, **kwargs):
    client = bigquery.Client()
    query = """
        SELECT *
        FROM `my-project-fastai-243607.aircondition.NewTaipei`
        """
    query_job = client.query(query,location="asia-east1") 
    aircondition=query_job.to_dataframe()
    context={} 
    context['object'] = HttpResponse(aircondition.to_html())
    return render(request, 'table.html', context)

class AnalysisView(View):
    template_name='analysis.html' 
    def get(self, request, id=None, *args, **kwargs):
        context={} 
        obj = get_object_or_404(Tables)
        context['object'] = obj
        return render(request, self.template_name, context)