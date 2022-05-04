import django
from django.db import models

# Create your models here.
class Book(models.Model):
    dat = django.utils.timezone.now()
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30, default="anonymous")
    genre = models.CharField(max_length=30, default="unknown")
    language = models.CharField(max_length=30, default="kazakh")
    country = models.CharField(max_length=30, default="Kazakhstan")
    year_published = models.DateField(default=dat)
    page_number = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['name', 'author']