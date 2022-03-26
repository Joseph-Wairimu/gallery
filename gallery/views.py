from django.shortcuts import render
from .models import Image, Category
# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'home.html',{'images': images[::-1], })



