from game import Game

board_to_load = []

with open('maps/basic_map', 'r') as f:
    for y, line in enumerate(f.readlines()):
        board_to_load.append([])
        for x, cell in enumerate(line):
            if cell != '\n':
                board_to_load[y].append(cell)

game = Game(board_to_load)

while True:
    game.display_map()
    print('w/a/s/d: ', end='')
    game.perform_action(input())