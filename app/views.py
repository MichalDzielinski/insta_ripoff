from django.shortcuts import render

def gallery(request):
    return render(request, 'gallery.html')

def viewPhoto(request, pk):
    return render(request, 'view.html')

def addPhoto(request):
    return render(request, 'add.html')