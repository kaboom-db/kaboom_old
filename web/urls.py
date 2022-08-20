from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('comics/', views.comics_index, name='comics_index'),
    path('comics/<int:comic_id>/', views.comic_detail, name='comic'),
    path('characters/<int:character_id>/', views.character_detail, name='character'),
]