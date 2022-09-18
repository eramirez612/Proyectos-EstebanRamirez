from contextvars import Context
from http.client import HTTPResponse
from pipes import Template
from pydoc import doc
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def index(request):
    return render(request, 'templateApp/index.html')

def renderTemplateJuguetes(request):
    return render(request, 'templateApp/juguete.html')

def renderTemplateRopa(request):
    return render(request, 'templateApp/ropa.html')

def usuario(request):
    doc_usuario = open('D:/Universidad/Proyectos-EstebanRamirez/Django_Evaluacion_1/Plantillas/templateApp/usuario.html')
    plantilla = Template(doc_usuario.read())
    doc_usuario.close()
    context = Context({'ID':'123456789-K','Nombre':'Dwayne Johnson','Correo':'omgistherock@gmail.com','Edad':'50'})
    doc = plantilla.render(context)
    return HttpResponse(doc)