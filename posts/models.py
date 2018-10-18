from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=3000)
    def __str__(self):
        return self.title
