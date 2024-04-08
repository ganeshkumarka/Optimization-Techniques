#Design a basic genetic algorithm to optimize a given objective function.
#The program should implement functionalities like selection, crossover, mutation,
#and generation replacement to find the optimal solution over multiple iterations.

import random

# Objective function (fitness function)
def objective_function(x):
    return x**2  # Example objective function: minimize x^2

# Initialization
def initialize_population(population_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

# Selection: Tournament selection
def tournament_selection(population, fitness_values, tournament_size):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: Bit flip mutation
def mutation(individual, mutation_rate):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(1 - gene)  # Flip the bit
        else:
            mutated_individual.append(gene)
    return mutated_individual

# Genetic algorithm
def genetic_algorithm(population_size, chromosome_length, generations, tournament_size, mutation_rate):
    # Initialization
    population = initialize_population(population_size, chromosome_length)
    for generation in range(generations):
        # Evaluation
        fitness_values = [objective_function(int(''.join(map(str, chromosome)), 2)) for chromosome in population]
        # Selection
        selected_population = tournament_selection(population, fitness_values, tournament_size)
        # Crossover
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])
        # Mutation
        population = [mutation(individual, mutation_rate) for individual in new_population]
    # Final evaluation
    best_individual = max(zip(population, fitness_values), key=lambda x: x[1])
    return best_individual

# Example usage
if __name__ == "__main__":
    population_size = 50
    chromosome_length = 10
    generations = 100
    tournament_size = 3
    mutation_rate = 0.1

    best_solution, best_fitness = genetic_algorithm(population_size, chromosome_length, generations, tournament_size, mutation_rate)
    print("Best solution:", ''.join(map(str, best_solution)))
    print("Best fitness:", best_fitness)
