from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import TemplateView, ListView
from .models import Image
from django.urls import reverse_lazy
from django.shortcuts import redirect

class IndexView(ListView):
    model = Image
    template_name = "ex/index.html"

class UploadImage(CreateView):
    template_name = "ex/upload.html"
    model = Image
    success_url = reverse_lazy("ex:index")
    fields = ['title', 'image']

class DeleteImage(DeleteView):
    model = Image
    success_url = reverse_lazy("ex:index")
