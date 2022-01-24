from unicodedata import category
from django.shortcuts import render, redirect
from .models import Photo, Category
from django.shortcuts import get_object_or_404

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        # better use the category id
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    ctx = {
        'categories' : categories,
        'photos' : photos,
    }
    return render(request, 'photos/gallery.html', ctx)

def viewPhoto(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    ctx = {
        'photo' : photo,
    }
    return render(request, 'photos/photo.html', ctx)

def AddPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            id = data['category']
            category = Category.objects.get(id=id)
        elif data['category_new'] != '':
            cat = data['category_new']
            category, created = Category.objects.get_or_create(name=cat)
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )

        return redirect('gallery')
    ctx = {
        'categories' : categories,
    }
    return render(request, 'photos/add.html', ctx)