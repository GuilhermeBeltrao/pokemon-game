import pickle
from pokemon import Pokemon, WaterTypePokemon, FireTypePokemon, EletricTypePokemon
from person import Person, Player, Enemy

def save_game(player):
    try:
        with open('pokemon-game/database.db', 'wb') as file:
            pickle.dump(player, file)
            print('O jogo foi salvo com sucesso')
    except Exception as error:
        print('erro ao salvar jogo: {}'.format(error))

def load_game():
    try:
        with open('pokemon-game/database.db', 'rb') as file:
            player = pickle.load(file)
            return player
    except Exception as error:
        print('erro ao carregar jogo: {} '.format(error))

if __name__ == '__main__':
    print('-----------------------------------------')
    print('Bem vindo ao pokemon RPG de terminal')
    print('-----------------------------------------')
    player = load_game() 
    if not player:
        name = input('Digite seu nome para comecar: ')
        player = Player(name)
        print('Ola {}, este e um mundo habitado por pokemons, sua missao e se tornar um mestre pokemon'.format(player))
        print('Capture o maximo de pokemons que conseguir e batalhe contra seus inimigos')
        print('')
        
        print("Você não tem nenhum pokemon, portanto precisa escolher um")
        player.choose_first_pokemon() 
        
        print("Pronto, agora que você já possui um pokemon, enfrente seu arqui-rival desde o jardim da infância Gary")
        gary = Enemy(name='Gary', pokemons=[WaterTypePokemon('Squirtle', level=1)])
        player.battle(gary)
        save_game(player)
        
    while True:
        print("--------------------------------------")
        print("O que deseja fazer?")
        print("1 - Explorar o mapa")
        print("2 - Lutar com um inimigo")
        print("3 - Ver seus Pokemons")
        print("0 - Sair do jogo")
        choice = input("Sua escolha: ")
        
        if choice == '0':
            print('Fechando jogo...')
            break
        elif choice == '1':
            player.explore_map()
            save_game(player)
        elif choice == '2':
            random_enemy = Enemy()
            player.battle(random_enemy)
            save_game(player)
        elif choice == '3':
            player.show_pokemons()
        
