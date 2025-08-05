import numpy as np
import random

def crossover(parent1_weights, parent2_weights):
    new_weights = []
    for w1, w2 in zip(parent1_weights, parent2_weights):
        shape = w1.shape
        flat1 = w1.flatten()
        flat2 = w2.flatten()

        cross_point = random.randint(0, len(flat1) - 1)
        child_flat = np.concatenate([flat1[:cross_point], flat2[cross_point:]])
        child = child_flat.reshape(shape)
        new_weights.append(child)
    return tuple(new_weights)

def mutate(weights, mutation_rate=0.05):
    new_weights = []
    for w in weights:
        shape = w.shape
        flat = w.flatten()
        for i in range(len(flat)):
            if random.random() < mutation_rate:
                flat[i] += np.random.normal()
        new_weights.append(flat.reshape(shape))
    return tuple(new_weights)

def select(population, scores, num_select):
    # Seleciona top N agentes por score
    sorted_pop = [agent for _, agent in sorted(zip(scores, population), key=lambda x: x[0], reverse=True)]
    return sorted_pop[:num_select]
