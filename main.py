import random
import pygame
import numpy as np
import matplotlib.pyplot as plt
from game import SnakeGame, UP, DOWN, LEFT, RIGHT
from agent import Agent
from genetic import crossover, mutate, select

POP_SIZE = 50
GENERATIONS = 50
MUTATION_RATE = 0.05
SELECTION_SIZE = 10
GRID_SIZE = 10

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake AI - Algoritmo Genético")
clock = pygame.time.Clock()

def get_state(game):
    head = game.snake[0]
    dir_left = (-game.direction[1], game.direction[0])
    dir_right = (game.direction[1], -game.direction[0])

    def danger(point):
        x, y = point
        return (x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE or point in game.snake)

    state = [
        danger((head[0] + game.direction[0], head[1] + game.direction[1])),  # perigo na frente
        danger((head[0] + dir_left[0], head[1] + dir_left[1])),             # perigo esquerda
        danger((head[0] + dir_right[0], head[1] + dir_right[1])),           # perigo direita

        game.direction == UP,
        game.direction == DOWN,
        game.direction == LEFT,
        game.direction == RIGHT,

        # Posição relativa da comida
        game.food[0] < head[0],  # comida à esquerda
        game.food[0] > head[0],  # comida à direita
        game.food[1] < head[1],  # comida acima
        game.food[1] > head[1],  # comida abaixo
    ]
    return np.array(state).astype(int)

def draw_game(game):
    block_size = WIDTH // (2 * GRID_SIZE)
    screen.fill((0, 0, 0))

    # Cobra
    for x, y in game.snake:
        pygame.draw.rect(screen, (0, 255, 0), (x * block_size, y * block_size, block_size, block_size))
    # Comida
    fx, fy = game.food
    pygame.draw.rect(screen, (255, 0, 0), (fx * block_size, fy * block_size, block_size, block_size))

def plot_progress(avg_scores):
    plt.clf()
    plt.title("Média de Pontuação por Geração")
    plt.xlabel("Geração")
    plt.ylabel("Pontuação Média")
    plt.plot(avg_scores, label='Avg Score')
    plt.legend()
    plt.pause(0.001)

def main():
    population = [Agent() for _ in range(POP_SIZE)]
    avg_scores = []

    for gen in range(GENERATIONS):
        scores = []
        for agent in population:
            game = SnakeGame()
            game.reset()
            max_steps = 200
            steps = 0

            while game.alive and steps < max_steps:
                state = get_state(game)
                action = agent.act(state)
                game.step(action)
                steps += 1

            scores.append(game.score)

        avg_score = sum(scores) / len(scores)
        avg_scores.append(avg_score)
        print(f"Geração {gen+1} - Score médio: {avg_score:.2f}")

        # Seleciona os melhores
        selected = select(population, scores, SELECTION_SIZE)

        # Gera nova população
        new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            child_weights = crossover(parent1.get_weights(), parent2.get_weights())
            child_weights = mutate(child_weights, MUTATION_RATE)
            child = Agent()
            child.set_weights(child_weights)
            new_population.append(child)

        population = new_population

        # Atualiza gráfico
        plot_progress(avg_scores)

    print("Treinamento concluído.")
    pygame.quit()

if __name__ == "__main__":
    main()
