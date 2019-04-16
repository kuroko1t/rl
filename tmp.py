import gym
import gym.spaces
import numpy as np
import common

class PointOnLine(gym.core.Env):
    def __init__(self):
        self.action_space = gym.spaces.Discrete(3)
        high = np.array([1, 0, 1])
        self.observation_space = gym.spaces.Box(low=-high, high=high)
        self.values_list = ''
        mean = np.average(self.values_list)
        std = np.std(self.values_list)
        self.values_list = (self.values_list - mean) / std

    def step(self, action):
        self.pos = self.values_list[self.index+self.step_num][0]
        done = self.step_num > 50
        if action == 2:
            reward = self.hold_val - self.pos
        elif action == 1:
            reward = self.pos - self.hold_val
        else:
            reward = 0
        self.step_num += 1
        return np.array([self.pos, self.hold, self.hold_val]), reward, done, {}

    def reset(self):
        self.index = int(np.random.randint(0,high=len(self.values_list)-50))
        self.pos = self.values_list[self.index][0]
        self.step_num = 0
        self.hold = 0
        self.hold_val = 0
        print(self.pos)
        return np.array([self.pos, self.hold, self.hold_val])
