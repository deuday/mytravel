from django.db import models


# Create your models here.
class host(models.Model):
    Name = models.CharField(max_length=350)
    Image = models.ImageField(upload_to='pic')
    dscrpt = models.TextField()


class own(models.Model):
    head = models.CharField(max_length=350)
    snap = models.ImageField(upload_to='pics')
    dsta = models.TextField()
