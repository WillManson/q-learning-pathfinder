import random
import math
import time
from game import Game
from file_manager import FileManager

class QLearner:
    def __init__(self, game, available_actions, discount_factor=0.9, learning_rate=0.9):
        self.game = game
        self.available_actions = available_actions
        dimensions = self.game.get_map_dimensions()
        self.q = [[[[0.0 for action in self.available_actions] for x in range(dimensions[1])] for y in range(dimensions[0])] for monster in range(26)]
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def perform_action(self, action):
        self.game.perform_action(action)
        if self.game.is_dead():
            return 'dead'
        elif self.game.has_won():
            return 'won'
        else:
            return 'nothing'

    def iterate(self):
        x = self.game.get_x()
        y = self.game.get_y()
        monster = self.game.get_relative_monster_location()
        action_index = self.choose_action()
        response = self.perform_action(self.available_actions[action_index])

        new_x = self.game.get_x()
        new_y = self.game.get_y()
        new_monster = self.game.get_relative_monster_location()

        reward = 0.0
        if response == 'dead':
            reward = -25.0
        elif response == 'won':
            reward = 100.0

        self.q[monster][y][x][action_index] = self.q[monster][y][x][action_index] + self.learning_rate * (reward + self.discount_factor * max(self.q[new_monster][new_y][new_x]) - self.q[monster][y][x][action_index])
        if response == 'dead' or response == 'won':
            print(response)
            self.game.respawn()

    def choose_action(self):
        q_list_at_pos = self.get_q_list_at_pos()
        q_list_at_pos = [math.exp(x) for x in q_list_at_pos]

        cumulative_sum = self.get_cumulative_sum(q_list_at_pos)

        random_num = random.random() * cumulative_sum[-1]
        action_index = 0
        while True:
            if action_index == len(q_list_at_pos) - 1:
                break
            elif random_num > cumulative_sum[action_index]:
                action_index += 1
            else:
                break

        return action_index

    def get_q_list_at_pos(self):
        return self.q[game.get_relative_monster_location()][game.get_y()][game.get_x()]

    def get_cumulative_sum(self, list_to_sum):
        cumulative_list = [ ]
        for i, x in enumerate(list_to_sum):
            cumulative_list.append(x if i == 0 else cumulative_list[i - 1] + x)
        return cumulative_list

random.seed()
available_actions = [ 'w', 'a', 's', 'd' ]
game = Game(FileManager().load_map('arena'))
learner = QLearner(game, available_actions)

while True:
    print()
    print('Options:')
    print('m: Output map')
    print('t: Train')
    print('r: Respawn')
    print('o: Output quantity data')
    print('q: Quit')
    choice = input('Choose: ')

    if choice == 'm':
        learner.game.display_map()
    elif choice == 't':
        num = input('Number of iterations: ')
        to_watch = input('Watch? y/n: ') == 'y'
        for i in range(int(num)):
            learner.iterate()
            if to_watch:
                learner.game.display_map()
                time.sleep(0.3)
    elif choice == 'r':
        learner.game.respawn()
    elif choice == 'o':
        print(learner.q)
    elif choice == 'q':
        break
