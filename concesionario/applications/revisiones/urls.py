from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('revisiones/', views.MostrarRevisiones.as_view() ),
    path('actualizarRevisiones/<pk>/', views.revisionesUpdateView.as_view() ),
    path('registrarR/', views.revisionesVista.as_view() ),

    
    

]
