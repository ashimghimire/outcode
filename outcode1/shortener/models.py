from django.db import models


class URL(models.Model):
    original_url = models.URLField(unique=True)  # To store the original long URL
    shortened_url = models.CharField(max_length=10, unique=True)  # To store the shortened URL

    def __str__(self):
        return self.original_url