class Game:
    def __init__(self, game_map):
        self.game_map = game_map

    def display_map(self):
        for y, row in enumerate(self.game_map):
            for x in row:
                print(self.style_map_detail(x), end='')
            print()

    def style_map_detail(self, detail):
        return {
            '0': '.',
            '1': 'O',
            '2': 'S',
            '3': 'E'
        }.get(detail, '?')
