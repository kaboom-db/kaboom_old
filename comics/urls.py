from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.comics_index, name='comics_index'),
    path('<int:comic_id>/', views.comic_detail, name='comic'),
]