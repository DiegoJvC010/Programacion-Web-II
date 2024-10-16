from django.urls import path
from . import views

urlpatterns = [
    path('obtener_estados/', views.obtener_estados, name='obtener_estados'),
    path('obtener_municipios/', views.obtener_municipios, name='obtener_municipios'),
]