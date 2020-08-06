from django.db import models

# Create your models here.

class Type(models.Model):
    # id = models.AutoField(primary_key=True)  # Django会自动创建,并设置为主键
    typename = models.CharField(max_length=20)

# 作品名称和作者(主演)
class Name(models.Model):
    # id 自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)


class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()

    class Meta:
        managed = False
        db_table = 't1'
