from flask import render_template, request
import requests
from app import app #from folder app, import app instance
from .forms import SearchForm

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    pokemon_name = None
    form = SearchForm()
    # Validate Form
    if form.validate_on_submit():
        pokemon_name = form.pokemon_name.data.lower()
        form.pokemon_name.data = '' #clear form after hitting search
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if not data:
                error_string = "Something went wrong. Couldn't connect the library."
                return render_template("pokemon.html.j2", form=form, error = error_string)
            
            pokemon_dict = {
                'pokemon_image': data['sprites']['other']['dream_world']['front_default'],
                'pokemon_name': data['name'],
                'ability_name': data['abilities'][0]['ability']['name'],
                'base_experience': data['base_experience'],
                'sprite_ULR': data['sprites']['front_shiny']
                }
            return render_template("pokemon.html.j2", form=form, pokemon = pokemon_dict)
        error_string = f'There is no pokemon named {pokemon_name}'
        return render_template("pokemon.html.j2", form=form, error=error_string)
    return render_template('pokemon.html.j2', form=form)
    
    
    
    
    
    
    
    
    
""""    
    if request.method == 'POST' and form.validate_on_submit():
        pokemon_name = form.pokemon_name.data.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if not data:
                error_string = f'There is no pokemon named {pokemon_name}'
                return render_template("pokemon.html.j2", form=form, error = error_string)

            pokemon_dict = {
                'pokemon_name': data['name'],
                'ability_name': data['abilities'][0]['ability']['name'],
                'base_experience': data['base_experience'],
                'sprite_ULR': data['sprites']['front_shiny']
                }
            return render_template('pokemon.html.j2',form=form, pokemon=pokemon_dict)
        else:
            error_string = "Something went wrong"
            render_template("pokemon.html.j2", form=form, error=error_string)
    return render_template('pokemon.html.j2', form=form)
"""