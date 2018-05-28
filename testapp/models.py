from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 100)

class Article(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    description = models.TextField()
