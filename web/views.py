from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from accounts.models import CustomUser
from kaboom.utils import get_user_image
from .forms import SignUpForm
from django.views import generic
from comics.models import Comic, Publisher, Character, Organisation, Creator, Genre

# Create your views here.
def home(request):
    # Either show the landing page if not logged in or redirect to user page
    if request.user.is_anonymous:
        comic_count = 0
        user_count = CustomUser.objects.count()
        ctx = {
            'header': '💥 KABOOM!',
            'active_home': 'active',
            'num_of_comics': comic_count,
            'num_of_users': user_count
        }
        return render(request, 'web/landing.html', context=ctx)
    else:
        return redirect('dashboard')

@login_required
def dashboard(request):
    image = get_user_image(request.user.email)
    return render(request, 'web/dashboard.html', {'image': image, 'active_home': 'active', 'header': 'Dashboard'})

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

########################################## COMIC STUFF ##########################################

def comics_index(request):
    # Get the last updated comics
    last_created = Comic.objects.all().order_by('-time_created')[:8]
    publishers = Publisher.objects.all()
    ctx = {
        'active_comics': 'active',
        'header': '📚 Comics',
        'last_created': last_created,
        'publishers': publishers
    }
    return render(request, 'comics/comics_index.html', context=ctx)

def comic_detail(request, comic_id):
    comic = get_object_or_404(Comic, id=comic_id)
    characters = comic.characters.values()
    genres = comic.genres.values()
    rating_colour = ''
    if comic.rating:
        if comic.rating > 6:
            rating_colour = 'rating-green'
        elif comic.rating > 3:
            rating_colour = 'rating-amber'
        else:
            rating_colour = 'rating-red'
    ctx = {
        'active_comics': 'active',
        'comic': comic,
        'characters': characters,
        'genres': genres,
        'rating_colour': rating_colour
    }
    return render(request, 'comics/comic_detail.html', context=ctx)

def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    comics = Comic.objects.filter(characters__in=[character.id])
    ctx = {
        'active_comics': 'active',
        'character': character,
        'comics': comics,
    }
    return render(request, 'comics/character_detail.html', context=ctx)