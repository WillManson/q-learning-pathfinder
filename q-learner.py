from game import Game
from file_manager import FileManager

class QLearner:
    def __init__(self, game):
        self.game = game
        dimensions = self.game.get_map_dimensions()
        self.reward_array = [[1.0 for x in range(dimensions[1])] for y in range(dimensions[0])]
        print(self.reward_array)

game = Game(FileManager().load_map('basic_map'))
learner = QLearner(game)
