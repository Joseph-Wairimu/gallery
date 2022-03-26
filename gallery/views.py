from django.shortcuts import render
from .models import Image, Category
# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'home.html',{'images': images[::-1], })



def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_articles = Image.search_by_category( category)
        message = f"{ category}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})