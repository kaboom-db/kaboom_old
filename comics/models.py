from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from common.models import Character, Creator, Genre

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Publisher, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comic(models.Model):
    STATUS = (
        ("Completed", "COMPLETED"),
        ("Releasing", "RELEASING"),
        ("Cancelled", "CANCELLED"),
        ("Planned", "PLANNED"),
    )

    FORMAT = (
        ("Comic", "COMIC"),
        ("Web Comic", "WEB COMIC"),
        ("Manga", "MANGA"),
    )

    name = models.CharField(max_length=100)
    summary = models.TextField()
    date_started = models.DateField(blank=True, null=True)
    date_finished = models.DateField(blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)
    cover_image = models.URLField(max_length=500, blank=True, null=True)
    banner_image = models.URLField(max_length=500, blank=True, null=True)
    creator = models.ForeignKey(Creator, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS)
    media_format = models.CharField(max_length=15, choices=FORMAT)
    comicvine_volume_id = models.PositiveIntegerField(blank=True, null=True)
    locg_series_id = models.PositiveIntegerField(blank=True, null=True)
    anilist_manga_id = models.PositiveIntegerField(blank=True, null=True)
    mal_manga_id = models.PositiveIntegerField(blank=True, null=True)
    tankobon_manga_id = models.PositiveIntegerField(blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True)
    characters = models.ManyToManyField(Character, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Comic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=100)
    comic_series = models.ForeignKey(Comic, on_delete=models.CASCADE)
    summary = models.TextField()
    absolute_number = models.PositiveIntegerField()
    volume_number = models.PositiveIntegerField(blank=True, null=True)
    page_count = models.PositiveIntegerField(blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    cover_image = models.URLField(max_length=500, blank=True, null=True)
    comicvine_issue_id = models.PositiveIntegerField(blank=True, null=True)
    locg_comic_id = models.PositiveIntegerField(blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.time_updated = timezone.now()
        super(Issue, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name