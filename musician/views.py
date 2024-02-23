from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms
from . import models




class add_musician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        return super().form_valid(form)