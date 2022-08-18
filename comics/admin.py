from django.contrib import admin
from .models import Comic, Publisher, Character, Organisation, Creator, Genre

# Register your models here.
admin.site.register(Comic)
admin.site.register(Publisher)
admin.site.register(Character)
admin.site.register(Organisation)
admin.site.register(Creator)
admin.site.register(Genre)