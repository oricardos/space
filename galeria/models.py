from django.db import models

class Article(models.Model):

    TAGS_OPTIONS = [
        ('NEBULOSA', 'Nebulosa'),
        ('GALAXIA', 'Galaxia'),
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=255, choices=TAGS_OPTIONS, default='')

    def __str__(self):
        return self.title
