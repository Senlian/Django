from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


# Create your models here.

class Image(models.Model):
    author = models.ForeignKey(User, related_name='image', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    url = models.URLField()
    slug = models.SlugField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
