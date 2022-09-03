from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('comics/', views.comics_index, name='comics_index'),

    path('comics/<int:comic_id>/', views.comic_redirect, name='comic_redirect'),
    path('comics/<int:comic_id>/<slug:slug>/', views.comic_detail, name='comic'),

    path('characters/<int:character_id>/<slug:slug>/', views.character_detail, name='character'),
    path('characters/<int:character_id>/', views.character_redirect, name='character_redirect'),

    path('publishers/<int:publisher_id>/<slug:slug>/', views.publisher_detail, name='publisher'),
    path('publishers/<int:publisher_id>/', views.publisher_redirect, name='publisher_redirect'),

    path('creators/<int:creator_id>/<slug:slug>/', views.creator_detail, name='creator'),
    path('creators/<int:creator_id>/', views.creator_redirect, name='creator_redirect'),
    
    path('teams/<int:team_id>/<slug:slug>/', views.team_detail, name='team'),
    path('teams/<int:team_id>/', views.team_redirect, name='team_redirect'),
    
    path('genres/<slug:slug>/', views.genre_detail, name='genre'),
]