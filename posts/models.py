from django.db import models
from markupfield.fields import MarkupField

class Category(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = MarkupField(markup_type='markdown')
    def __str__(self):
        return self.title
