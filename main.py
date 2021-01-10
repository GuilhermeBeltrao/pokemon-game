from pokemon import Pokemon, WaterTypePokemon, FireTypePokemon, EletricTypePokemon
from person import Person, Player, Enemy

def choose_first_pokemon(player):
    print('Ola {}! Escolha o pokemon que ira te acompanhar em sua jornada'.format(player))
    
    pikachu_inicial = EletricTypePokemon('Pikachu', level=1)
    charmander_inicial = FireTypePokemon('Charmander', level=1)
    squirtle_inicial = WaterTypePokemon('Squirtle', level=1)
    print('Voce possui 3 escolhas de pokemon')
    print('1 - ', pikachu_inicial)
    print('2 - ', charmander_inicial)
    print('3 - ', squirtle_inicial)

    while True:
        choice = input('Escolha seu pokemon: ')

        if choice == '1':
            player.capture_pokemon(pikachu_inicial)
            break
        elif choice == '2':
            player.capture_pokemon(charmander_inicial)
            break
        elif choice == '3':
            player.capture_pokemon(squirtle_inicial)
            break
player = Player('Guilherme')
player.capture_pokemon(FireTypePokemon('Charmander', level=1))

test_enemy = Enemy(name=None, pokemons=[WaterTypePokemon('Squirtle', level=1)])

player.battle(test_enemy)