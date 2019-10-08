from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Postres

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import utils

# Create your views here.
class PostresListado(ListView):
    model = Postres

class PostreDetalle(DetailView):
    model = Postres

class PostreCrear(SuccessMessageMixin, CreateView):
    model = Postres
    form = Postres
    fields = "__all__"
    success_message = 'Postre creado correctamente!'

    def get_success_url(self):
        return reverse('leer')

class PostreActualizar(SuccessMessageMixin,UpdateView):
    model =  Postres
    form = Postres
    fields = "__all__"
    success_message = 'Postre actualizado correctamente!'

    def get_success_url(self):
        return reverse('leer')

class PostreEliminar(SuccessMessageMixin,DeleteView):
    model = Postres
    form = Postres
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Postre eliminado correctamente!'
        messages.success(self.request,(success_message))
        return reverse('leer')