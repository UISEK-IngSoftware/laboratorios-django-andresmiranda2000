from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'trainers', views.TrainerViewSet)

pokemon_list = views.PokemonViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

pokemon_detail = views.PokemonViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

trainer_list = views.TrainerViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
    }
)

trainer_detail = views.TrainerViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

urlpatterns = [
    path('pokemons', pokemon_list, name='pokemon-list-no-slash'),
    path('pokemons/<int:pk>', pokemon_detail, name='pokemon-detail-no-slash'),
    path('trainers', trainer_list, name='trainer-list-no-slash'),
    path('trainers/<int:pk>', trainer_detail, name='trainer-detail-no-slash'),
    path('', include(router.urls)),
]