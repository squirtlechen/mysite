from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
from google.cloud import bigquery

# Create your views here.

def table_view(request, *args, **kwargs):
    client = bigquery.Client()
    query = """
        SELECT *
        FROM `my-project-fastai-243607.aircondition.NewTaipei`
        """
    query_job = client.query(query,location="asia-east1") 
    aircondition=query_job.to_dataframe()
    final_table=aircondition.to_html()
    return HttpResponse(final_table)

