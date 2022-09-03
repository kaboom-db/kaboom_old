from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone

from accounts.models import CustomUser
from kaboom.utils import get_user_image, util_calculate_age
from .forms import SignUpForm
from django.views import generic
from comics.models import Comic, Publisher, Character, Organisation, Creator, Genre

# Create your views here.
def home(request):
    # Either show the landing page if not logged in or redirect to user page
    if request.user.is_anonymous:
        comic_count = Comic.objects.count()
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

def comic_redirect(request, comic_id):
    comic = get_object_or_404(Comic, id=comic_id)
    return redirect('comic', comic_id=comic.id, slug=comic.slug)

def comic_detail(request, comic_id, slug):
    comic = get_object_or_404(Comic, id=comic_id, slug=slug)
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

def character_redirect(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return redirect('character', character_id=character.id, slug=character.slug)

def character_detail(request, character_id, slug):
    character = get_object_or_404(Character, id=character_id, slug=slug)
    comics = Comic.objects.filter(characters__in=[character.id])
    teams = Organisation.objects.filter(characters__in=[character.id])
    ctx = {
        'active_comics': 'active',
        'character': character,
        'comics': comics,
        'teams': teams
    }
    return render(request, 'comics/character_detail.html', context=ctx)

def publisher_redirect(request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    return redirect('publisher', publisher_id=publisher.id, slug=publisher.slug)

def publisher_detail(request, publisher_id, slug):
    publisher = get_object_or_404(Publisher, id=publisher_id, slug=slug)
    comics = Comic.objects.filter(publisher=publisher.id)
    ctx = {
        'active_comics': 'active',
        'publisher': publisher,
        'comics': comics,
    }
    return render(request, 'comics/publisher_detail.html', context=ctx)

def creator_redirect(request, creator_id):
    creator = get_object_or_404(Creator, id=creator_id)
    return redirect('creator', creator_id=creator.id, slug=creator.slug)

def creator_detail(request, creator_id, slug):
    creator = get_object_or_404(Creator, id=creator_id, slug=slug)
    comics = Comic.objects.filter(creator=creator.id)
    age = None
    if creator.date_of_birth:
        if creator.date_of_death:
            age = util_calculate_age(creator.date_of_birth, creator.date_of_death)
        else:
            age = util_calculate_age(creator.date_of_birth, timezone.now().date())
    ctx = {
        'active_comics': 'active',
        'creator': creator,
        'comics': comics,
        'age': age,
    }
    return render(request, 'comics/creator_detail.html', context=ctx)

def team_redirect(request, team_id):
    team = get_object_or_404(Organisation, id=team_id)
    return redirect('team', team_id=team.id, slug=team.slug)

def team_detail(request, team_id, slug):
    team = get_object_or_404(Organisation, id=team_id, slug=slug)
    characters = team.characters.values()
    ctx = {
        'active_comics': 'active',
        'team': team,
        'characters': characters,
    }
    return render(request, 'comics/team_detail.html', context=ctx)

def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    comics = Comic.objects.filter(genres__in=[genre.id])
    ctx = {
        'active_comics': 'active',
        'header': genre.name,
        'genre': genre,
        'comics': comics,
    }
    return render(request, 'comics/genre_detail.html', context=ctx)