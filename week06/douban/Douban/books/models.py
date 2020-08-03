from django.db import models

# Create your models here.
class Name(models.Model):
    # id 自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=5)

class Comment(models.Model):
    # id 自动创建
    context = models.TextField()
    stars = models.CharField(max_length=5)