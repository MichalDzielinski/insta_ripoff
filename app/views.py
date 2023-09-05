from django.shortcuts import render, redirect
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
    category = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != "":
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image=image
        )

        return redirect('gallery')
    
    context = {'category': category}
    return render(request, 'add.html', context)