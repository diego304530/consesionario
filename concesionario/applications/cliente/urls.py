from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('clienteingreso/', views.clienteVista.as_view() ),
    path('listarcliente/', views.Mostrarc.as_view() ),
    path('actualizarcliente/<pk>/', views.clienteUpdateView.as_view()),

]
