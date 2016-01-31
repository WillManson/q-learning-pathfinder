from game import Game
from file_manager import FileManager

game = Game(FileManager().load_map('basic_map'))

while True:
    game.display_map()
    print('w/a/s/d: ', end='')
    game.perform_action(input())
