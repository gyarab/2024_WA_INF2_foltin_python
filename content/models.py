from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    category = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:20]


