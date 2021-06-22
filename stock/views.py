from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from stock.models import Producto
from stock.forms import ProductosFormulario

class index(ListView):
    model = Producto
    template_name = 'datatable.html'


class CrearProductos(CreateView):
    model = Producto
    form_class = ProductosFormulario
    template_name = 'añadirproducto.html'
    success_url = '/'


class EditarProductos(UpdateView):
    model = Producto
    form_class = ProductosFormulario
    template_name = 'editarproductos.html'
    success_url = '/'


class EliminarProductos(DeleteView):
    model = Producto
    template_name = "eliminarproducto.html"
    success_url = '/'
