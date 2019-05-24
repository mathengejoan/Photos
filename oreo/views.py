from django.shortcuts import render,get_object_or_404, redirect
from .models import Album,Images
from .forms import AlbumForm
# Create your views here.
def index(request):
    albums = Album.objects.filter(user=request.user)
    context = {'albums':albums}
    return render(request,'oreo/index.html',context)

def add_album(request):
    form = AlbumForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        album = form.save(commit=False)
        album.cover = request.FILES['cover']
        album.user=request.user
        album.save()
        return render(request, 'oreo/details.html', {'album':album})
    return render(request, 'oreo/add_album.html',{'form': form})

def details(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'oreo/details.html', {'album': album})
