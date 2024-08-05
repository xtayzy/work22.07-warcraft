from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title


class Screenshot(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='screenshots/')

    def __str__(self):
        return self.title


class Cinematic(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')


class GameProcess(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')


class Location(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='locations/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='music/')


class Company(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='companies/')

    def __str__(self):
        return self.title


class Characters(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='characters/')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Background(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.title

