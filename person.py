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
    
    def __init__(self, name=None, pokemons=[], money=100, pokeballs=10):
        if name:
            self.name = name
        else: 
            self.name = random.choice(NAMES)
        
        self.pokemons = pokemons
        self.money = money
        self.pokeballs = pokeballs
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
                choice = input('escolha seu pokemon: ')
                try:
                    int_choice = int(choice)
                    chosen_pokemon = self.pokemons[int_choice]
                    print('{} escolheu {}'.format(self, chosen_pokemon))
                    return chosen_pokemon
                except:
                    print('escolha invalida')
        else:
            print('este jogador nao possui nenhum pokemon para batalhar')
            
            
    def battle(self, person):
        print('{} desafiou {} para uma batalha!'.format(self, person))
        person.show_pokemons()
        enemy_pokemon = person.choose_pokemon()
        player_pokemon = self.choose_pokemon()
        
        if player_pokemon and enemy_pokemon:
            while True:    
                if player_pokemon.attack(enemy_pokemon):
                    print('{} ganhou a batalha!'.format(player_pokemon))
                    self.earn_money(15)
                    break
        
                elif enemy_pokemon.attack(player_pokemon):
                    print('{} ganhou a batalha'.format(enemy_pokemon))
                    self.earn_money(-15)
                    break
        else:
            print('Essa batalha nao pode ocorrer')            
       
    def earn_money(self, amount):
        self.money += amount
        if amount > 0:
            print('Voce ganhou {} moedas. Total: {}'.format(amount, self.money))   
        elif amount < 0:
            print('Voce perdeu {} moedas. Total: {}'.format(amount, self.money))
    
        
class Player(Person):
    type = 'player'
    
    def capture_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        capture_choice = input('voce deseja gastar uma pokebola para capturar este pokemon? (sim/nao) ')
        if capture_choice == 'sim' or capture_choice == 'Sim':
            print("{} capturou {}".format(self, pokemon))
        else:
            print('O pokemon fugiu')

    def explore_map(self):
        if random.random() <= 0.3:
            wild_pokemon = random.choice(POKEMONS)
            print('um {} selvagem apareceu'.format(wild_pokemon)) 
            self.capture_pokemon(wild_pokemon)
        else:
            print('essa exploracao nao deu em nada')
            
    def choose_first_pokemon(self):
        pikachu_inicial = EletricTypePokemon('Pikachu', level=1)
        charmander_inicial = FireTypePokemon('Charmander', level=1)
        squirtle_inicial = WaterTypePokemon('Squirtle', level=1)
        print('Voce possui 3 escolhas de pokemon: ')
        print('1 - ', pikachu_inicial)
        print('2 - ', charmander_inicial)
        print('3 - ', squirtle_inicial)

        while True:
            choice = input('Escolha seu pokemon: ')
            if choice == '1':
                self.capture_pokemon(pikachu_inicial)
                break
            elif choice == '2':
                self.capture_pokemon(charmander_inicial)
                break
            elif choice == '3':
                self.capture_pokemon(squirtle_inicial)
                break
            
            
class Enemy(Person):
    type = 'enemy'

    def __init__(self, name=None, pokemons=None):

        if not pokemons:
            for i in range(random.randint(1,6)):
                random_pokemons = []
                random_pokemons.append(random.choice(POKEMONS))
                super().__init__(name=name, pokemons=random_pokemons)
        
        else:
            super().__init__(name=name, pokemons=pokemons)
    
    def choose_pokemon(self):
        if self.pokemons:
            chosen_pokemon = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self,chosen_pokemon))
            return chosen_pokemon
        else: 
            print('erro: Este jogador nao possui pokemons')
    
