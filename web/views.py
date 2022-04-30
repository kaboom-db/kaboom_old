from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from comics.models import Comic
from accounts.models import CustomUser
from kaboom.utils import get_user_image

# Create your views here.
def home(request):
    # Either show the landing page if not logged in or redirect to user page
    comic_count = Comic.objects.count()
    user_count = CustomUser.objects.count()
    ctx = {
        'header': '💥 KABOOM!',
        'num_of_comics': comic_count,
        'num_of_users': user_count
    }
    return render(request, 'web/landing.html', context=ctx)

@login_required
def dashboard(request):
    image = get_user_image(request.user.email)
    return render(request, 'web/dashboard.html', {'image': image})