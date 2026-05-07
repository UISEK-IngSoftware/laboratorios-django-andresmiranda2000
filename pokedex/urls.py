from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("pokemon/agregar/", views.add_pokemon, name="add_pokemon"),
    path("pokemon/<int:id>/editar/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemon/<int:id>/eliminar/", views.delete_pokemon, name="delete_pokemon"),
    path("trainers/", views.trainer_list, name="trainer_list"),
    path("trainer/<int:id>/", views.trainer, name="trainer"),
]
