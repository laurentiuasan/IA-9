import numpy as np


class Cliff:
    def __init__(self):
        self.board = np.zeros([4, 12])
        self.board[3, 1:11] = -1
        self.start_position = (3, 0)
        self.goal_position = (3, 11)

    def __str__(self):
        return [str(i) for i in self.board]


class Agent:
    def __init__(self):
        self.cliff = Cliff()
        self.actions = ["up", "down", "left", "right"]
        self.states = []
        self.position = self.cliff.start_position
        self.state_actions = {}
        for i in range(4):
            for j in range(12):
                self.state_actions[(i, j)] = {}
                for a in self.actions:
                    self.state_actions[(i, j)][a] = 0

    def choose_action(self):
        action = ""
        max_reward = -9999
        for a in self.actions:
            current_position = self.position
            reward = self.state_actions[current_position][a]
            if reward >= max_reward:
                action = a
                max_reward = reward
        return action

    def __str__(self):
        return self.states.__str__()


if __name__ == '__main__':
    agent = Agent()
    print(agent)