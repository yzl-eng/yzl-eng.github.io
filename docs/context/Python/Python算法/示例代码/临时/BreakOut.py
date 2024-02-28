

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import sys
import matplotlib.pyplot as plt
from collections import deque

MAX_MEMORY = 3000
BATCH_SIZE = 300
LR = 0.0003 # 学习率，自己看着改吧
EPSILON = 0.0
GAMMA = 0.9
Rep = 0
SAVE = 400
SHOW = 200


class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Sequential(
            nn.Linear(20, 128, bias=True),
            nn.ReLU()
        )
        self.hidden1 = nn.Sequential(
            nn.Linear(128, 16, bias=True),
            nn.ReLU()
        )
        self.out = nn.Sequential(
            nn.Linear(16, 4, bias=True)
        )

    def init_weights(self, m):
        if type(m) == nn.Conv2d:
            m.weight.data.normal_(0.01, 0.02)
        if type(m) == nn.Linear:
            torch.nn.init.xavier_uniform_(m.weight)
            m.bias.data.fill_(0.01)

    def forward(self, x):
        x = self.hidden(x)
        x = self.hidden1(x)
        x=self.out(x)
        return x


class QTrainer(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.lr = LR
        self.gamma = GAMMA
        self.model = model
        self.optimizer = optim.AdamW(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)  # .cuda()
        next_state = torch.tensor(next_state, dtype=torch.float)  # .cuda()
        action = torch.tensor(action, dtype=torch.long)  # .cuda()
        reward = torch.tensor(reward, dtype=torch.float)  # .cuda()

        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            if not done: next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done,)

        predict = self.model(state)

        target = predict.clone()

        for i in range(len(done)):
            if done[i]:
                Q_new = reward[i]
            else:
                Q_new = reward[i] + self.gamma * torch.max(self.model(torch.unsqueeze(next_state[i], 0)))

            target[i][action[i]] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, predict)
        loss.backward()
        self.optimizer.step()


class IllegalMoveError(BaseException):
    pass


class SnakeGame():
    def __init__(self):
        self.init()

    def init(self):
        self.score = 0
        self.steps = 0
        self.time = 50
        self.snake_board = np.zeros((16, 16), dtype=np.float32)
        self.snake = deque()
        self.p = random.randint(0, 15)
        self.q = random.randint(0, 15)
        self.snake_board[self.p][self.q] = 1
        self.snake.append((self.p, self.q))
        self.DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.place_food()
        self.eaten = False

    def place_food(self):
        self.i = random.randint(0, 15)
        self.j = random.randint(0, 15)

    def get_state(self):
        incoord = lambda m,n: m in range(0,16) and n in range(0,16)
        grid = lambda m,n: self.snake_board[m+self.p][n+self.q] if incoord(m+self.p, n+self.q) else 0

        return np.array([
            grid(-2, 0),
            grid(-1, -1), grid(-1, 0), grid(-1, 1),
            grid(0, -2), grid(0, -1), grid(0, 0), grid(0, 1), grid(0, 2),
            grid(1, -1), grid(1, 0), grid(1, 1),
            grid(2, 0),
            self.p, self.q, 15-self.p, 15-self.q,
            self.p-self.i, self.q-self.j, self.time
        ], dtype=np.float32)

    def move(self, direction):

        # move
        self.p, self.q = self.snake[-1]
        self.p += self.DIRECTIONS[direction][0]
        self.q += self.DIRECTIONS[direction][1]
        self.time -= 1
        if not (0 <= self.p < 16 and 0 <= self.q < 16): raise IllegalMoveError
        if self.time < 0: raise TimeoutError
        self.snake.append((self.p, self.q))
        if not self.eaten: self.snake.popleft()

        # judge food
        self.eaten = False
        food_pos = (self.i, self.j)
        for a in self.snake:
            if a == food_pos:
                self.eaten = True
                self.score += 1
                self.time = 50 + self.score
                self.place_food()
                break

        # judge if self collide
        i = 2 if self.eaten else 1
        self.snake_board = np.zeros((16, 16), dtype=np.float32)
        for (p, q) in self.snake:
            if self.snake_board[p][q] != 0:
                raise IllegalMoveError
            self.snake_board[p][q] = i
            i += 1

        self.steps += 1
        return self.eaten


class Agent:

    def __init__(self):

        self.epsilon = EPSILON  # randomness
        self.gamma = GAMMA  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # popleft()
        self.load_model()
        self.trainer = QTrainer(self.model)
        # self.trainer.cuda()
        self.game = SnakeGame()

        # self.graph_init()

    def load_model(self):
        try:
            with open('./epoch.txt', 'r', encoding='utf8') as fp:
                self.epoch = int(fp.readline())
                fp.close()
                self.model = torch.load(f'./{self.epoch}.bin')
                self.model.eval()
        except:
            self.epoch = 1
            self.model = DQN()

    def save_model(self):
        with open('./epoch.txt', 'w', encoding='utf8') as fp:
            fp.write(str(self.epoch))
            fp.close()
            torch.save(self.model, f'./{self.epoch}.bin')

    def graph_init(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-0.5, 15.5)
        self.ax.set_ylim(-0.5, 15.5)
        self.ax.plot(0, 0)
        self.fig.canvas.draw()

    def train_long_memory(self):
        if len(self.memory) != 0:
            states, actions, rewards, next_states, dones = zip(*(self.memory))
            self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        # self.memory.append((state, action, reward, next_state, done))
        if reward == 0:
            if random.randint(1,10) == 1: self.memory.append((state, action, reward, next_state, done))
        else:
            self.memory.append((state, action, reward, next_state, done))
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        if self.epoch <= 1500:
            if random.randint(0,19) == 0:
                return random.randint(0, 3)
        elif self.epoch <= 5000:
            if random.randint(0,49) == 0:
                return random.randint(0, 3)
        elif self.epoch <= 15000:
            if random.randint(0,299) == 0:
                return random.randint(0, 3)
        state = torch.tensor(state)  # .cuda()
        state = torch.unsqueeze(state, 0)
        prediction = self.model(state)
        move = torch.argmax(prediction).item()
        return move

    def update_ui(self):
        snake_head_x = self.game.snake[-1][0]
        snake_head_y = self.game.snake[-1][1]
        point_list_x = [x for (x, y) in self.game.snake]
        point_list_y = [y for (x, y) in self.game.snake]
        plt.cla()
        self.ax.plot(point_list_x, point_list_y, 'r-', snake_head_x, snake_head_y, 'go',
                     self.game.i, self.game.j, 'bo')
        plt.draw()
        self.ax.set_xlim(-0.5, 15.5)
        self.ax.set_ylim(-0.5, 15.5)
        plt.pause(0.03)

    def train(self):
        while True:
            self.game.init()
            if self.epoch % SHOW == 0:
                self.graph_init()
            reward = 0
            done = False
            state = self.game.get_state()
            next_state = self.game.get_state()
            while not done:
                state = self.game.get_state()
                action = self.get_action(state)
                try:
                    eaten = self.game.move(action)
                except IllegalMoveError:
                    reward = -20
                    done = True
                except TimeoutError:
                    reward = -25
                    done = True
                else:
                    if self.epoch % SHOW == 0:
                        self.update_ui()
                    reward = 40 * int(eaten)
                    next_state = self.game.get_state()
                self.train_short_memory(state, action, reward, next_state, done)
            if self.epoch % SHOW == 0:
                plt.pause(1)
                plt.close()

            self.train_long_memory()
            print(self.epoch, self.game.score, self.game.steps)

            if self.epoch % SAVE == 0:
                self.save_model()

            self.epoch += 1


if __name__ == '__main__':
    agent = Agent()
    agent.train()