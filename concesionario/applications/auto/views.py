from django.shortcuts import render

from .models import Autos
from django.views.generic import TemplateView, ListView
# Create your views here.


class listarAutoView(ListView):
    model = Autos
    template_name = "auto_dis.html"
    context_object_name = 'Auto'

