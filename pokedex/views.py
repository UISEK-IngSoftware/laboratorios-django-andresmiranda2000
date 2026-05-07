from django.shortcuts import render, get_object_or_404, redirect

from .models import Pokemon, Trainer
from .forms import PokemonForm


def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})


def pokemon(request, id):
    poke = get_object_or_404(Pokemon, id=id)
    return render(request, 'display_pokemon.html', {'pokemon': poke})


def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm()
    return render(request, 'add_pokemon.html', {'form': form})


def edit_pokemon(request, id):
    poke = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=poke)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm(instance=poke)
    return render(request, 'edit_pokemon.html', {'form': form, 'pokemon': poke})


def delete_pokemon(request, id):
    poke = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        poke.delete()
        return redirect('index')
    return render(request, 'delete_pokemon.html', {'pokemon': poke})


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers})


def trainer(request, id):
    trainer_obj = get_object_or_404(Trainer, id=id)
    return render(request, 'display_trainer.html', {'trainer': trainer_obj})
