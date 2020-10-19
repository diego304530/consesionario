from django.shortcuts import render 
from django.http import request
from.models import Clientes
from applications.cochesVendidos.models import CochesVendidos 
from django.views.generic import  TemplateView ,ListView , CreateView, UpdateView


# Create your views here.




class clienteUpdateView(UpdateView):
    template_name = "cliente/updateCl.html"
    model = Clientes
    fields=("__all__")
    success_url='/listarcliente/'

class clienteVista(CreateView):
    
    model = Clientes
    template_name = "cliente/inicio.html"
    fields=('__all__')
    success_url='.'


class Mostrarc(ListView):
    c1= CochesVendidos.objects.prefetch_related()
    queryset=c1
    fields=('__all__')
    template_name = "cliente/mostrar.html"
    context_object_name = 'listar'

