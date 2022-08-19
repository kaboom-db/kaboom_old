from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Creator(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    is_adult = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    ALIGNMENT_CHOICES = (
        ("Good", "GOOD"),
        ("Evil", "EVIL"),
        ("Antihero", "ANTIHERO"),
    )

    CHARACTER_STATUS_CHOICES = (
        ("Alive", "ALIVE"),
        ("Deceased", "DECEASED"),
        ("Unknown", "UNKNOWN"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    alias = models.CharField(max_length=100, blank=True, null=True)
    alignment = models.CharField(max_length=15, choices=ALIGNMENT_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=15, choices=CHARACTER_STATUS_CHOICES, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    intelligence = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    strength = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    speed = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    durability = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    power = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    combat = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    is_adult = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.URLField(max_length=500, blank=True, null=True)
    disbanded = models.BooleanField(default=False)
    characters = models.ManyToManyField(Character, blank=True)
    is_adult = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    is_adult = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comic(models.Model):
    MEDIA_STATUS_CHOICES = (
        ("Completed", "COMPLETED"),
        ("Releasing", "RELEASING"),
        ("Cancelled", "CANCELLED"),
        ("Planned", "PLANNED"),
    )

    MEDIA_FORMATS = (
        ("Comic", "COMIC"),
        ("Web Comic", "WEB COMIC"),
        ("Manga", "MANGA"),
        ("Manhwa", "MANHWA"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateField(blank=True, null=True)
    date_finished = models.DateField(blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)
    cover_image = models.URLField(max_length=750, blank=True, null=True)
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=15, choices=MEDIA_STATUS_CHOICES)
    media_format = models.CharField(max_length=15, choices=MEDIA_FORMATS)
    chapter_count = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)
    characters = models.ManyToManyField(Character, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    is_adult = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name