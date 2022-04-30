from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Base)
admin.site.register(models.Character)
admin.site.register(models.Creator)
admin.site.register(models.Genre)
admin.site.register(models.Team)
admin.site.register(models.VoiceActor)