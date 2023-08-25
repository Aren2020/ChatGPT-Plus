from django.db import models
from django.utils.text import slugify

class Section(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
