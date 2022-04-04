from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    # Titulo do post.
    title = models.CharField(max_length=300)
    # Slug será a Url do post.
    slug = models.SlugField(max_length=300, unique=True, auto_created=title)
    # Autor do post.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Texto do post
    body = models.TextField()
    # Data de criação do post
    created = models.DateTimeField(auto_now_add=True)
    # Data de atualização do post.
    update = models.DateTimeField(auto_now=True)

    class meta: # Definindo a ordem do último post para o primeiro.
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})