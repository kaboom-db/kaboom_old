from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from comics.models import Comic, Publisher, Character, Organisation, Creator

register = template.Library()

@register.simple_tag()
def itemcard(image, name, itemid, itemslug, view):
    if not image:
        image = staticfiles_storage.url('images/noimage.png')

    link = reverse(view, args=[itemid, itemslug])

    return mark_safe(f"""
    <a href="{link}" class="link sm-card-link" title="{name}">
        <div class="info-card sm-card-result">
            <div class="sm-card-img-container">
                <img src="{image}" alt="{name} image" class="sm-card-img">
            </div>
            <div class="card-body info-card-body">
                <div class="sm-card-name">
                    <center>
                        <h5 class="card-title" style="font-size: smaller; margin: 0px;">{name}</h5>
                    </center>
                </div>
            </div>
        </div>
    </a>
    """)