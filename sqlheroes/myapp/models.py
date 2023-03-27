from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    world = models.ForeignKey(
        'World',
        on_delete=models.CASCADE,
        null=True
    )

class AbilityType(models.Model):
    name = models.CharField(max_length=123)

class World(models.Model):
    name = models.CharField(max_length=123)