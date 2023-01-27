from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Article(models.Model):

    TAGS_OPTIONS = [
        ('NEBULOSA', 'Nebulosa'),
        ('GALAXIA', 'Galaxia'),
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image_file = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    image_url = models.CharField(max_length=255, null=False, blank=True)
    category = models.CharField(max_length=255, choices=TAGS_OPTIONS, default='')
    is_posted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.title
