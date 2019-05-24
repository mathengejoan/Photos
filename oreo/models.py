from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    year = models.CharField(max_length=40)
    cover = models.ImageField()

    def __str__(self):
        return self.name


