from django.shortcuts import render, redirect
from serial_app.models import reserva
from serial_app.forms import FormReservas

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def listadoreservas(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarreserva(request):
    form = FormReservas()
    if request.method == "POST":
        form = FormReservas(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)

def eliminarReserva(request, id):
    res = reserva.objects.get(id = id)
    res.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    res = reserva.objects.get(id = id)
    form = FormReservas(instance = res)
    if request.method == 'POST':
        form = FormReservas(request.POST, instance=res)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)
