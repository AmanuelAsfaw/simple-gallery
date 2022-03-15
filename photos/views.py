# from curses.ascii import HT
# from django.shortcuts import render
from ast import arg
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Gallery

# Create your views here.
def index(request):
    galleries = Gallery.objects.order_by('title')[:5]
    template = loader.get_template('photos/index.html')
    context = {
        'galleries': galleries,
    }
    return render(request, 'photos/index.html',context)

def detail(request, gallery_id):
    try:
        gallery = Gallery.objects.get(pk=gallery_id)
    except Gallery.DoesNotExist:
        raise Http404("Gallery does not exist123")
    return render(request, 'photos/detail.html', {'gallery': gallery})

def photos(request, gallery_id):
    response = "You're looking at the photos of gallery %s."
    return HttpResponse(response % gallery_id)

def owner(request, gallery_id):
    return HttpResponse("You're looking on owner of gallery %s." % gallery_id)

def add_gallery(request):
    context = {}
    return render(request, 'photos/add.html',context)

def add_gallery_post(request):
    try:
        title = request.POST['title']
        description = request.POST['description']
        gallery = Gallery()
        gallery.title = title
        gallery.description = description
        gallery.save()
        return HttpResponseRedirect(reverse('photos:gallery_detail', args=(gallery.id,)))

    except Exception as e:
         return HttpResponse(str(e))