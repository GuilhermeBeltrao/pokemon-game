import random


class Pokemon:

    #       Constructor
    def __init__(self, species, level=None, name=None):
        self.type = type
        self.species = species
        
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
            
        if name:
            self.name = name
        else:
            self.name = species
            
    def __str__(self):
        return "{} ({})".format(self.name, self.level)

    def attack(self, pokemon):
        print("{} atacou {}!".format(self.name, pokemon.name))
        
    # begin type subclass -->       
class EletricTypePokemon(Pokemon):
    type = 'eletric'
    def attack(self, pokemon):
        print('{} deixou {} em shockkk'.format(self, pokemon))

class WaterTypePokemon(Pokemon):
    type = 'water'
    def attack(self, pokemon):
        print('{} obrigou {} a jogar baleia azul'.format(self, pokemon))

class FireTypePokemon(Pokemon):
    type = 'fire'
    def attack(self, pokemon):
        print('{} apagou um cigarro na testa do {}'.format(self, pokemon))

   # <-- end type subclass     
   
