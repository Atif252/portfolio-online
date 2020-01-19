from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
	file_path = 'blog/{title}-{filename}'.format(
			title=str(instance.title), filename=filename
		)
	return file_path




class BlogPost(models.Model):
    title           = models.CharField(max_length=2000, null=False, blank=False)
    body            = models.TextField(null=False, blank=False, max_length=10000)
    image           = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published  = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    slug            = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def slug(self):
        return self.slug