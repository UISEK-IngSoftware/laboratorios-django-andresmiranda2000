from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    pokemons = models.ManyToManyField(Pokemon, blank=True, related_name='trainers')

    def __str__(self):
        return self.name