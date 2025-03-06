from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:20]

