from django.db import models
from markupfield.fields import MarkupField

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkupField(markup_type='markdown')
    def __str__(self):
        return self.title
