from django.shortcuts import render
from django.http import JsonResponse
import json
import os

# Cargar los datos del archivo JSON
def cargar_datos():
    ruta_archivo = os.path.join(os.path.dirname(__file__),'data', 'estados-municipios.json')
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

datos_estados_municipios = cargar_datos()

# Vista para obtener los estados
def obtener_estados(request):
    estados = list(datos_estados_municipios.keys())
    return JsonResponse({'estados': estados})

# Vista para obtener municipios según el estado seleccionado
def obtener_municipios(request):
    estado = request.GET.get('estado')
    municipios = datos_estados_municipios.get(estado, [])
    return JsonResponse({'municipios': municipios})