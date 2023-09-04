from django.shortcuts import render
from .models import Category, Photo

def gallery(request):
    category = Category.objects.all()
    photos = Photo.objects.all()
    context = {'photos': photos, 'category': category}
    return render(request, 'gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'view.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'add.html')