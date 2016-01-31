import sys

class Game:
    def __init__(self, game_map):
        self.game_map = game_map
        self.player_pos = self.find_start_position()

    def display_map(self, show_player=True):
        for y, row in enumerate(self.game_map):
            for x, cell in enumerate(row):
                if show_player and (y, x) == self.player_pos:
                    print('X', end='')
                else:
                    print(self.style_map_detail(cell), end='')
            print()

    def get_map_dimensions(self):
        return (len(self.game_map), len(self.game_map[0]))

    def style_map_detail(self, detail):
        return {
            '0': '.',
            '1': 'O',
            '2': 'S',
            '3': 'E'
        }.get(detail, '?')

    def find_start_position(self):
        for y, row in enumerate(self.game_map):
            for x, cell in enumerate(row):
                if cell == '2':
                    return (y, x)
        print('No start position set')
        sys.exit(1)

    def is_dead(self):
        return self.game_map[self.get_y()][self.get_x()] == '0'

    def has_won(self):
        return self.game_map[self.get_y()][self.get_x()] in [ '3' ]

    def respawn(self):
        self.player_pos = self.find_start_position()

    def get_y(self):
        return self.player_pos[0]

    def get_x(self):
        return self.player_pos[1]

    def perform_action(self, action):
        if action == 'w':
            self.player_pos = (self.get_y() - 1, self.get_x())
        elif action == 's':
            self.player_pos = (self.get_y() + 1, self.get_x())
        elif action == 'a':
            self.player_pos = (self.get_y(), self.get_x() - 1)
        elif action == 'd':
            self.player_pos = (self.get_y(), self.get_x() + 1)
        else:
            print('Invalid action')
