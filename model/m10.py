#Implement a basic genetic algorithm in Python to optimize a 
#simple function (e.g., finding the minimum of a quadratic equation).
import random
import math

# Objective function: Quadratic equation f(x) = ax^2 + bx + c
def objective_function(x, a, b, c):
    return a * x**2 + b * x + c

# Initialization: Generate initial population
def initialize_population(population_size, min_value, max_value):
    return [random.uniform(min_value, max_value) for _ in range(population_size)]

# Selection: Tournament selection
def tournament_selection(population, fitness_values, tournament_size):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
        winner = min(tournament, key=lambda x: x[1])[0]  # Minimize objective function
        selected.append(winner)
    return selected

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: Random perturbation
def mutation(individual, mutation_rate, min_value, max_value):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            perturbation = random.uniform(-0.1, 0.1)  # Small random change
            mutated_gene = gene + perturbation
            mutated_gene = max(min_value, min(mutated_gene, max_value))  # Clamp value within bounds
            mutated_individual.append(mutated_gene)
        else:
            mutated_individual.append(gene)
    return mutated_individual

# Genetic algorithm
def genetic_algorithm(objective_function, population_size, min_value, max_value, generations, tournament_size, mutation_rate, a, b, c):
    # Initialization
    population = initialize_population(population_size, min_value, max_value)
    for generation in range(generations):
        # Evaluation
        fitness_values = [objective_function(x, a, b, c) for x in population]
        # Selection
        selected_population = tournament_selection(population, fitness_values, tournament_size)
        # Crossover
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])
        # Mutation
        population = [mutation(individual, mutation_rate, min_value, max_value) for individual in new_population]
    # Final evaluation
    best_individual = min(zip(population, fitness_values), key=lambda x: x[1])  # Minimize objective function
    return best_individual

# Example usage
if __name__ == "__main__":
    population_size = 50
    min_value = -10
    max_value = 10
    generations = 100
    tournament_size = 3
    mutation_rate = 0.1
    a = 1
    b = -2
    c = 1

    best_solution, best_fitness = genetic_algorithm(objective_function, population_size, min_value, max_value, generations, tournament_size, mutation_rate, a, b, c)
    print("Best solution:", best_solution)
    print("Best fitness:", best_fitness)
