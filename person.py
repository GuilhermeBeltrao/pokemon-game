from pokemon import WaterTypePokemon, FireTypePokemon, EletricTypePokemon

class Person:
    
    def __init__(self, name=None, pokemons=[]):
        if name:
            self.name = name
        else: 
            self.name = 'Desconhecido'
        
        self.pokemons = pokemons
    
    def __str__(self):
        return self.name
    
    def show_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)
            

class Player(Person):
    type = 'player'

class Enemy(Person):
    type = 'enemy'

player_pokemon1 = EletricTypePokemon('pikachu', 1)
player_pokemon2 = WaterTypePokemon('squirtle', 2)
player_pokemon3 = FireTypePokemon('charmander', 1)

player = Player(name='Guilherme', pokemons=[player_pokemon1, player_pokemon2, player_pokemon3])

print(player)
player.show_pokemons()