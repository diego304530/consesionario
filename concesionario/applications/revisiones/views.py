from django.shortcuts import render
from django.views.generic import  TemplateView ,ListView , CreateView, UpdateView
# Create your views here.
from.models import Revisiones

# Create your views here.

class MostrarRevisiones(ListView):
    c1= Revisiones.objects.prefetch_related()
    queryset=c1
    fields=('__all__')
    template_name = "revisiones/mostrar.html"
    context_object_name = 'listar'

class revisionesUpdateView(UpdateView):
    template_name = "revisiones/updateR.html"
    model = Revisiones
    fields=("__all__")
    success_url='/revisiones/'
    

class revisionesVista(CreateView):
    
    model = Revisiones
    template_name = "revisiones/revisiones.html"
    fields=('__all__')
    success_url='.'
