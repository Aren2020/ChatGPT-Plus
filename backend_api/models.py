from django.db import models
from django.utils.text import slugify

class Section(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ApiStatus(models.Model):
    api = models.CharField(max_length = 200)
    starttime = models.CharField(default = 'NONTOUCH', max_length = 50)
    trycount = models.IntegerField(default = 0) 
    status = models.BooleanField(default = True)
    disable = models.BooleanField(default = False) 

    class Meta:
        verbose_name_plural = 'ApiStatus'