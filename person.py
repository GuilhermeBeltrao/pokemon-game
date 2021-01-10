import random

from pokemon import WaterTypePokemon, FireTypePokemon, EletricTypePokemon


NAMES = ['Gary', 'Dave', 'Bob', 'Donald', 'Tracy', 'Megan', 'Susan']

POKEMONS = [
    #   Fire pokemons
    FireTypePokemon('Flareon'), FireTypePokemon('Charmander'), 
    FireTypePokemon('Cyndaquil'), FireTypePokemon('Chimchar'),
    
    #   Water pokemons
    WaterTypePokemon('Squirtle'), WaterTypePokemon('Psyduck'),
    WaterTypePokemon('Horsea'), WaterTypePokemon('Croconaw'),
    
    #   Eletric pokemons
    EletricTypePokemon('Pikachu'), EletricTypePokemon('Elekid'),
    EletricTypePokemon('Shinx'), EletricTypePokemon('Voltorb')
]
class Person:
    
    def __init__(self, name=None, pokemons=[]):
        if name:
            self.name = name
        else: 
            self.name = random.choice(NAMES)
        
        self.pokemons = pokemons
    
    def __str__(self):
        return self.name
    
    def show_pokemons(self):
        if self.pokemons:
            print('pokemons de {}'.format(self))
            for i, pokemon in enumerate(self.pokemons):   
                print('{} - {}'.format(i, pokemon))
        else:
            print('{} nao tem nenhum pokemon'.format(self))
            
    def choose_pokemon(self):
        self.show_pokemons()
        if self.pokemons:
            while True:
                try:
                    choice = input('escolha seu pokemon: ')
                    choice = int(choice)
                    chosen_pokemon = self.pokemons[choice]
                    return chosen_pokemon
                except:
                    print('escolha invalida')
        else:
            print('este jogador nao possui nenhum pokemon para batalhar')
    def battle(self, person):
        print('{} desafiou {} para uma batalha!'.format(self, person))
        person.show_pokemons()
        self.choose_pokemon()
        
        while True:
            choice = input('Escolha seu pokemon: ')

            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '3':
                pass
        
class Player(Person):
    type = 'player'
    
    def capture_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))
        
class Enemy(Person):
    type = 'enemy'

    def __init__(self, name=None, pokemons=[]):
        super().__init__(name=name, pokemons=pokemons) 
        #   super() puxa a funcao init de pessoa, para nao repetir codigo

        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
                #   escolhe entre 1 e 6 pokemons aleatorios 
                #   e adiciona a lista de pokemons do inimigo
    
