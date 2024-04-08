#Design a genetic algorithm for a specific optimization
# problem (e.g., job scheduling) with appropriate fitness 
#function and crossover operators.

import numpy as np

# Define job scheduling problem parameters
num_jobs = 5
num_time_slots = 10
max_generations = 100
population_size = 50
mutation_rate = 0.1

# Define job processing times (example)
processing_times = np.random.randint(1, 10, size=num_jobs)

def initialize_population():
    """Initialize the population with random schedules."""
    return np.random.randint(2, size=(population_size, num_jobs, num_time_slots))

def fitness(schedule):
    """Calculate the fitness of a schedule (makespan)."""
    completion_times = np.zeros(num_jobs)
    for i in range(num_jobs):
        for j in range(num_time_slots):
            if schedule[i, j] == 1:
                completion_times[i] += processing_times[i]
    return np.max(completion_times)

def crossover(parent1, parent2):
    """Perform crossover (single-point crossover)."""
    crossover_point = np.random.randint(1, num_time_slots)
    child1 = np.hstack((parent1[:, :crossover_point], parent2[:, crossover_point:]))
    child2 = np.hstack((parent2[:, :crossover_point], parent1[:, crossover_point:]))
    return child1, child2

def mutate(schedule):
    """Perform mutation (random bit flip)."""
    mutated_schedule = schedule.copy()
    for i in range(num_jobs):
        for j in range(num_time_slots):
            if np.random.random() < mutation_rate:
                mutated_schedule[i, j] = 1 - mutated_schedule[i, j]  # Flip bit
    return mutated_schedule

def select_parents(population):
    """Select parents using tournament selection."""
    num_parents = 2
    selected_parents = []
    for _ in range(num_parents):
        indices = np.random.choice(range(population_size), size=5, replace=False)
        selected_parents.append(population[np.argmin([fitness(population[i]) for i in indices])])
    return selected_parents

def genetic_algorithm():
    """Main genetic algorithm loop."""
    # Initialize population
    population = initialize_population()

    # Evolution loop
    for generation in range(max_generations):
        # Select parents
        parents = select_parents(population)

        # Perform crossover and mutation
        offspring = []
        for parent1, parent2 in zip(parents[::2], parents[1::2]):
            child1, child2 = crossover(parent1, parent2)
            offspring.extend([mutate(child1), mutate(child2)])

        # Replace old population with offspring
        population[:len(offspring)] = offspring

        # Print best fitness in current generation
        best_fitness = min([fitness(schedule) for schedule in population])
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    # Select best schedule from final population
    best_schedule = population[np.argmin([fitness(schedule) for schedule in population])]
    print("Optimal Schedule:", best_schedule)
    print("Optimal Makespan:", fitness(best_schedule))

# Run the genetic algorithm
genetic_algorithm()
