from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Create your models here.
class Base(models.Model):
    nation = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Comic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class VoiceActor(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Comic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Character(models.Model):
    ALIGNMENT = (
        ("Good", "GOOD"),
        ("Evil", "EVIL"),
        ("Anti-Hero", "ANTIHERO")
    )

    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField()
    alignment = models.CharField(max_length=15, choices=ALIGNMENT, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    intelligence = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    strength = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    speed = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    durability = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    power = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    combat = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, blank=True, null=True)
    voice_actors = models.ManyToManyField(VoiceActor, blank=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Comic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, blank=True, null=True)
    logo = models.URLField(max_length=500, blank=True, null=True)
    disbanded = models.BooleanField(default=False)
    characters = models.ManyToManyField(Character)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Comic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Creator(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Comic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name