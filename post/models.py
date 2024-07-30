from django.db import models
from author.models import Author

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(Author, related_name='author', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='Criado em: ', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em: ', auto_now=True)
    published_at = models.DateTimeField(verbose_name='Publicado em: ', null=True, blank=True)
    is_published = models.BooleanField(default=False)