from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(unique=True, max_length=500)
    sub_title = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_published = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='img/posts/', blank=True, null=True)

    slug = models.SlugField(editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def publish(self):
        self.date_published = timezone.now()

