from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Photo
from django.shortcuts import render

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()

        context = {
            'photos': photos
        }

        return context