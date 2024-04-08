#Write a program to implement a simple genetic algorithm 
#for a specific optimization problem (e.g., finding the maximum value of a function). 
#The program should initialize a population of solutions, apply selection, crossover, 
#and mutation operators, and iterate until a stopping criterion is met (e.g., reaching a desired fitness level).

import numpy as np

# Define the objective function
def objective_function(x):
    return x**2 - 4*x + 4

# Define the range of possible solutions
solution_space = (-10, 10)

# Genetic Algorithm Parameters
population_size = 50
num_generations = 100
mutation_rate = 0.1

# Initialization
def initialize_population():
    return np.random.uniform(*solution_space, size=population_size)

# Fitness calculation
def calculate_fitness(population):
    return objective_function(population)

# Selection
def selection(population, fitness):
    # Select parents based on fitness proportionate selection
    probabilities = fitness / np.sum(fitness)
    return np.random.choice(population, size=2, p=probabilities)

# Crossover
def crossover(parent1, parent2):
    # Single-point crossover
    crossover_point = np.random.randint(1, len(parent1))
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# Mutation
def mutation(child):
    # Random mutation by adding a small random value
    if np.random.rand() < mutation_rate:
        return child + np.random.uniform(-0.5, 0.5)
    return child

# Genetic Algorithm
def genetic_algorithm():
    # Initialize population
    population = initialize_population()

    # Evolution loop
    for generation in range(num_generations):
        # Evaluate fitness
        fitness = calculate_fitness(population)

        # Select parents
        parents = [selection(population, fitness) for _ in range(population_size // 2)]

        # Perform crossover and mutation
        offspring = [mutation(child) for parent_pair in parents for child in crossover(*parent_pair)]

        # Combine parents and offspring
        population = np.concatenate((population, offspring))

        # Select top individuals for the next generation
        population = sorted(population, key=objective_function, reverse=True)[:population_size]

        # Print best fitness in current generation
        best_fitness = max(fitness)
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    # Select best solution from final population
    best_solution = max(population, key=objective_function)
    best_fitness = objective_function(best_solution)
    print(f"Optimal Solution: {best_solution}, Optimal Fitness: {best_fitness}")

# Run the genetic algorithm
genetic_algorithm()
