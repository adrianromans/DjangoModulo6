from django.shortcuts import render
from django.contrib import messages

from .forms import VehiculoForm


# Create your views here.
def index_View(request):        
    return render(request, 'index.html',{})

def addVehiculo (request):
    form = VehiculoForm (request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success (request, 'Los Datos se han procesado exitosamente!!')
        
    return render(request, "addform.html", {'form': form})