from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('obtener_estados/', views.obtener_estados, name='obtener_estados'),
    path('obtener_municipios/', views.obtener_municipios, name='obtener_municipios'),
    path('estados_municipios/', TemplateView.as_view(template_name="zonas/estados_municipios.html"), name='estados_municipios'),
]