from django.shortcuts import render
from gallery.models import Gallery


def home(request):
	gallerys = Gallery.miaoshu
    return render(request, 'home.html', {'gallerys': gallerys})