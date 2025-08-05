import random

GRID_SIZE = 10

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(5, 5)]
        self.direction = RIGHT
        self.spawn_food()
        self.alive = True
        self.steps = 0
        self.score = 0

    def spawn_food(self):
        while True:
            self.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if self.food not in self.snake:
                break

    def step(self, action):  # ação: 0 = frente, 1 = direita, 2 = esquerda
        self.steps += 1
        self.move(action)
        reward = 0

        head = self.snake[0]
        if head == self.food:
            self.snake.append(self.snake[-1])
            self.score += 1
            self.spawn_food()
            reward = 10
        else:
            self.snake.pop()

        if (head in self.snake[1:] or
            not 0 <= head[0] < GRID_SIZE or
            not 0 <= head[1] < GRID_SIZE):
            self.alive = False
            reward = -10

        return reward

    def move(self, action):
        idx = DIRECTIONS.index(self.direction)
        if action == 1:  # direita
            idx = (idx + 1) % 4
        elif action == 2:  # esquerda
            idx = (idx - 1) % 4
        self.direction = DIRECTIONS[idx]
        head = self.snake[0]
        dx, dy = self.direction
        new_head = (head[0] + dx, head[1] + dy)
        self.snake = [new_head] + self.snake
