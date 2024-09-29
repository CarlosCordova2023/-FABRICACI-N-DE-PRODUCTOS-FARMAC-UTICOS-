from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Laboratorio
from .forms import LaboratorioForm

from .models import Producto, DirectorGeneral
from .forms import ProductoForm, DirectorGeneralForm


# Vista para la página de inicio
def index(request):
    return render(request, 'laboratorio/index.html')


# Leer (Mostrar la lista de laboratorios)
def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})

# Crear (Insertar un laboratorio)
def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

# Actualizar (Editar un laboratorio)
def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

# Eliminar un laboratorio
def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_list')
    return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})



# CRUD para Productos
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'laboratorio/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'laboratorio/producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'laboratorio/producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'laboratorio/producto_confirm_delete.html', {'producto': producto})

# CRUD para Directores Generales
def directorgeneral_list(request):
    directores_generales = DirectorGeneral.objects.all()
    return render(request, 'laboratorio/directorgeneral_list.html', {'directores_generales': directores_generales})

def directorgeneral_create(request):
    if request.method == 'POST':
        form = DirectorGeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directorgeneral_list')
    else:
        form = DirectorGeneralForm()
    return render(request, 'laboratorio/directorgeneral_form.html', {'form': form})

def directorgeneral_update(request, pk):
    directorgeneral = get_object_or_404(DirectorGeneral, pk=pk)
    if request.method == 'POST':
        form = DirectorGeneralForm(request.POST, instance=directorgeneral)
        if form.is_valid():
            form.save()
            return redirect('directorgeneral_list')
    else:
        form = DirectorGeneralForm(instance=directorgeneral)
    return render(request, 'laboratorio/directorgeneral_form.html', {'form': form})

def directorgeneral_delete(request, pk):
    directorgeneral = get_object_or_404(DirectorGeneral, pk=pk)
    if request.method == 'POST':
        directorgeneral.delete()
        return redirect('directorgeneral_list')
    return render(request, 'laboratorio/directorgeneral_confirm_delete.html', {'directorgeneral': directorgeneral})