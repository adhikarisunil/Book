from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Nobel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Poem(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    type = models.TextField()