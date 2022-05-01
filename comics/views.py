from django.shortcuts import render

from . import models

# Create your views here.
def comics_index(request):
    # Get the last updated comics
    last_created = models.Comic.objects.all().order_by('-time_created')[:8]
    new_issues = models.Issue.objects.all().order_by('-time_created')[:8]
    publishers = models.Publisher.objects.all()
    ctx = {
        'active_comics': 'active',
        'header': '📚 Comics',
        'last_created': last_created,
        'new_issues': new_issues,
        'publishers': publishers
    }
    return render(request, 'comics/comics_index.html', context=ctx)