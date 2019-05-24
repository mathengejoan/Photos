from django.shortcuts import render, get_object_or_404, redirect
from .models import Images
from .forms import ImageForm


# Create your views here.
def index(request):
    images = Images.objects.filter(user=request.user)
    context = {'images': images}
    return render(request, 'oreo/index.html', context)


def add_images(request):
    form = ImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        images = form.save(commit=False)
        images.cover = request.FILES['cover']
        images.user = request.user
        images.save()
        return render(request, 'oreo/details.html', {'images': images})
    return render(request, 'oreo/add_images.html', {'form': form})

