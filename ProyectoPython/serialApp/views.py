from django.shortcuts import render, redirect
from serialApp.models import User, Proyecto
from serialApp.forms import ProyectoForm
from django.views.generic import ListView, View
from django.http import HttpResponse
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def personadata(request):
    personas = Proyecto.objects.all()
    data = {'personas' : personas}
    return render(request, 'empleados.html', data)

def index(request):
    return render(request, 'index.html')

def listadoproyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'proyectos.html', data)

def agregarproyecto(request):
    form = ProyectoForm()
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)

def eliminarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    pro.delete()
    return redirect('/proyectos')

def actualizarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    form = ProyectoForm(instance=pro)
    if request.method == 'POST':
        form = ProyectoForm(request.POST,request.FILES, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'actualizarProyecto.html', data)

class ProyectoPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('serialApp/template/lista.html')
        context = {'title': 'Primer PDF'}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response