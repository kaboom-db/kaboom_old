from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from comics.models import Comic
from accounts.models import CustomUser
from kaboom.utils import get_user_image
from .forms import SignUpForm
from django.views import generic

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