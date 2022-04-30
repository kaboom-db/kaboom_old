from django.shortcuts import render

# Create your views here.
def home(request):
    # Either show the landing page if not logged in or redirect to user page
    return render(request, 'web/landing.html', context={'header': '💥 KABOOM!'})