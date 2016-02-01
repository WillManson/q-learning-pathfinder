import sys
import random

class Game:
    def __init__(self, game_map):
        self.game_map = game_map
        self.player_pos = self.find_position('2')
        self.has_monster = self.check_has_monster()
        if self.has_monster:
            self.monster_pos = self.find_position('4')

    def display_map(self, show_player=True):
        for y, row in enumerate(self.game_map):
            for x, cell in enumerate(row):
                if show_player and (y, x) == self.player_pos:
                    print('X', end='')
                elif self.has_monster and show_player and (y, x) == self.monster_pos:
                    print('M', end='')
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
            '3': 'E',
            '4': 'P'
        }.get(detail, '?')

    def find_position(self, to_find):
        for y, row in enumerate(self.game_map):
            for x, cell in enumerate(row):
                if cell == to_find:
                    return (y, x)
        print('No position set')
        sys.exit(1)

    def check_has_monster(self):
        for row in self.game_map:
            if '4' in row:
                return True
        return False

    def get_relative_monster_location(self):
        relative_x = self.player_pos[1] - self.monster_pos[1]
        relative_y = self.player_pos[0] - self.monster_pos[0]
        if (abs(relative_x) >= 3 or abs(relative_y) >= 3):
            return 25
        return 5 * (relative_x + 2) + relative_y + 2

    def is_dead(self):
        return (self.game_map[self.get_y()][self.get_x()] == '0' or self.has_hit_monster())

    def has_won(self):
        return self.game_map[self.get_y()][self.get_x()] in [ '3' ]

    def respawn(self):
        self.player_pos = self.find_position('2')

    def get_y(self):
        return self.player_pos[0]

    def get_x(self):
        return self.player_pos[1]

    def update_monster(self):
        if self.has_monster:
            random_num = random.random()
            if random_num < 0.25:
                self.monster_pos = (self.monster_pos[0] + 1, self.monster_pos[1])
            elif random_num < 0.50:
                self.monster_pos = (self.monster_pos[0] - 1, self.monster_pos[1])
            elif random_num < 0.75:
                self.monster_pos = (self.monster_pos[0], self.monster_pos[1] + 1)
            else:
                self.monster_pos = (self.monster_pos[0], self.monster_pos[1] - 1)
            if self.game_map[self.monster_pos[0]][self.monster_pos[1]] == '0':
                self.respawn_monster()

    def respawn_monster(self):
        self.monster_pos = self.find_position('4')

    def has_hit_monster(self):
        if self.has_monster:
            return (self.player_pos[0] == self.monster_pos[0] and self.player_pos[1] == self.monster_pos[1])
        return False

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
        self.update_monster()
