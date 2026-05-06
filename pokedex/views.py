from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


def trainer_list(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainers.html')
    return HttpResponse(template.render({'trainers': trainers}, request))


def trainer(request, id: int):
    trainer_obj = get_object_or_404(Trainer, id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer_obj
    }
    return HttpResponse(template.render(context, request))