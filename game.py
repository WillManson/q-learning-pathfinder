import sys

class Game:
    def __init__(self, game_map):
        self.game_map = game_map
        self.player_pos = self.find_start_position()

    def display_map(self):
        for row in self.game_map:
            for cell in row:
                print(self.style_map_detail(cell), end='')
            print()

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
        print("No start position set")
        sys.exit(1)
