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
        
        #   battle attributes
        self.attack_damage = self.level * 5
        self.life = self.level * 10 
                
    def __str__(self):
        return "{} ({})".format(self.name, self.level)

    def attack(self, pokemon):
        #   interacoes de tipos
        real_damage = int(self.attack_damage * random.random() * 1.3)
        print("{} atacou {}! (dano = {})".format(self.name, pokemon.name, real_damage))
        pokemon.life -= real_damage
        print('')
        print('{} perdeu {} de vida'.format(pokemon, real_damage))    
        print('vida atual de {}: {}'.format(pokemon, pokemon.life))
        if pokemon.life <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else: 
            return False
        
        
    # begin type subclass -->       
class EletricTypePokemon(Pokemon):
    type = 'eletric'
    def attack(self, pokemon):
        print('{} deixou {} em shockkk'.format(self, pokemon))
        return super().attack(pokemon)

class WaterTypePokemon(Pokemon):
    type = 'water'
    def attack(self, pokemon):
        print('{} obrigou {} a jogar baleia azul'.format(self, pokemon))
        return super().attack(pokemon)

class FireTypePokemon(Pokemon):
    type = 'fire'
    def attack(self, pokemon):
        print('{} apagou um cigarro na testa do {}'.format(self, pokemon))
        return super().attack(pokemon)

   # <-- end type subclass     
   
