from django.shortcuts import render, redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models

class add_album(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        return super().form_valid(form)


class edit_album(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

class delete_album(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'