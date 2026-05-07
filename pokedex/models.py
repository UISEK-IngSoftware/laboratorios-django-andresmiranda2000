from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    TYPE_CHOICES = [
        ('Fuego', 'Fuego'),
        ('Agua', 'Agua'),
        ('Planta', 'Planta'),
        ('Eléctrico', 'Eléctrico'),
        ('Normal', 'Normal'),
        ('Psíquico', 'Psíquico'),
        ('Hielo', 'Hielo'),
        ('Lucha', 'Lucha'),
        ('Veneno', 'Veneno'),
        ('Tierra', 'Tierra'),
        ('Volador', 'Volador'),
        ('Bicho', 'Bicho'),
        ('Roca', 'Roca'),
        ('Fantasma', 'Fantasma'),
        ('Dragón', 'Dragón'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    weight = models.FloatField()
    height = models.FloatField()
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='pokemons')
    photo = models.ImageField(upload_to='pokemon_photos/', null=True, blank=True)

    def __str__(self):
        return self.name