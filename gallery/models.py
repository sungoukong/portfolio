from django.db import models

# Create your models here.


class Gallery(models.Model):
	miaoshu = models.CharField(max_length=100)