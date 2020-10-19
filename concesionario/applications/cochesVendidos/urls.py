from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('cochesVendidos/', views.cochesVista.as_view() ),
    
    path('actualizarCoches/<pk>/', views.cochesUpdateView.as_view()),

]
