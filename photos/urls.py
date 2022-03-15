from django.urls import path

from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /photos/5/
    path('gallery/<int:gallery_id>/', views.detail, name='gallery_detail'),
    # ex: /add/
    path('gallery/add/', views.add_gallery, name='gallery_add'),
    # ex: /add/
    path('gallery/add/submit', views.add_gallery_post, name='gallery_add_post'),
    # ex: /photos/5/photos/
    path('gallery/<int:gallery_id>/photos/', views.photos, name='gallery_photos'),
    # ex: /photos/5/vote/
    path('gallery/<int:gallery_id>/owner/', views.owner, name='gallery_owner'),
]