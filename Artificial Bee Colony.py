import numpy as np

Constants
COLONY_SIZE = 10
DIMENSIONS = 2
MAX_ITERATIONS = 10
PHI = 0.1  # Pheromone factor

Objective function (e.g., Sphere function)
def objective_function(solution):
    return np.sum(solution**2)

Initialize pheromone matrix
pheromone_matrix = np.ones((COLONY_SIZE, DIMENSIONS))

Initialize food sources (solutions)
food_sources = np.random.uniform(-5, 5, (COLONY_SIZE, DIMENSIONS))

Initialize best solution
best_solution = np.zeros(DIMENSIONS)
best_fitness = np.inf

for iteration in range(MAX_ITERATIONS):
    for i in range(COLONY_SIZE):
        new_solution = food_sources[i] + np.random.uniform(-1, 1, DIMENSIONS)
        new_fitness = objective_function(new_solution)
        pheromone_matrix[i] += PHI * (1 / (1 + new_fitness))
        if new_fitness < objective_function(food_sources[i]):
            food_sources[i] = new_solution
            if new_fitness < best_fitness:
                best_solution = new_solution
                best_fitness = new_fitness

print("Best solution:", best_solution)
print("Best fitness:", best_fitness)