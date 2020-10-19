from django.shortcuts import render


from.models import CochesVendidos

from django.views.generic import  TemplateView ,ListView , CreateView, UpdateView






class cochesUpdateView(UpdateView):
    template_name = "coches/updateCoches.html"
    model = CochesVendidos
    fields=("__all__")
   
    success_url='/listarcliente/' 
    

class cochesVista(CreateView):
    
    model = CochesVendidos
    template_name = "coches/cochesVendidos.html"
    fields=('__all__')
    success_url='.'
