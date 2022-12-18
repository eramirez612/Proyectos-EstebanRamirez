from django.shortcuts import render, redirect
from .serializers import InscritosSerializer, InstitucionesSerializers
from .models import Inscritos, Instituciones
from .forms import FormInscritos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')
    
def listadoReservas(request):
    ins = Inscritos.objects.all()
    data = {'ins': ins}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormInscritos()
    if request.method == "POST":
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)

def eliminarReserva(request, id):
    ins = Inscritos.objects.get(id = id)
    ins.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormInscritos(instance = ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'actualizarreserva.html', data)

#-------------------------------------------------------------------------JSON---------------------------------------------------------------------------#
def inscritosDB(request):
    ins = Inscritos.objects.all()
    data = {'DJANGO_SEMINARIO' : list(ins.values('id', 'nombre', 'institucion', 'telefono', 'fechareserva', 'horareserva', 'estado', 'observacion'))}
    
    return JsonResponse(data)

#--------------------------------------------------------------------Funcion Based View------------------------------------------------------------------#
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        insti = Instituciones.objects.all()
        serial = InstitucionesSerializers(insti, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionesSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        insti = Instituciones.objects.get(pk=id)
    except insti.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionesSerializers(insti)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InscritosSerializer(insti, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        insti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# ----------------------------------------------------------------------Class Based Views----------------------------------------------------------------#
class ListaInscritos(APIView):
    def get(self, request):
        ins = Inscritos.objects.all()
        serial = InscritosSerializer(ins, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscritos(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(id=pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins)
        return Response(serial.data)

    def put(self, request, pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ins = self.get_object(pk)
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)