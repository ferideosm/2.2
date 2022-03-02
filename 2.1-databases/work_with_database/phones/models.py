from django.db import models
from datetime import date
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True) 
    price = models.PositiveIntegerField(default=0) 
    image = models.CharField(max_length=100,  blank=True, null=True) 
    release_date = models.DateField(default=date.today)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)