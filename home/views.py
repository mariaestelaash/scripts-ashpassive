from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .clean_columns import sort_by_location, clean_unnecessary_collumns
import pandas as pd 
from django.views.generic.base import TemplateView
from django import forms
import io

from django.shortcuts import render
from django.views.generic.base import View

# from .forms import ImportForm, ProductForm
class UploadFileForm(forms.Form):
    file = forms.FileField()

class ImportView(TemplateView):
    template_name = "home/main.html"
    def index(self, request):
        return render(request,self.template_name)
    def post(self, request):  
        context = {
            'messages':[]
        }
        archive_name = request.POST.get("archive_name")
       
        csv = request.FILES['csv']
        print(csv)
        csv_data = pd.read_csv( io.StringIO(
                csv.read().decode("utf-8")
            ))
        new_df = sort_by_location(csv_data)
        clean_unnecessary_collumns(new_df,archive_name)

        return render(request,self.template_name,context)
                      