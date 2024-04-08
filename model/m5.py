import numpy as np

def nearest_neighbor_tsp(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    tour = []
    
    # Start from the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    # Find nearest neighbor for each city
    for _ in range(num_cities - 1):
        min_distance = float('inf')
        nearest_city = None
        
        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                min_distance = distance_matrix[current_city][city]
                nearest_city = city
        
        # Move to the nearest unvisited city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
    
    # Return the tour
    return tour

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)
    
    # Calculate total distance by summing distances between consecutive cities
    for i in range(num_cities):
        total_distance += distance_matrix[tour[i - 1]][tour[i]]  # Distance from previous city to current city
    
    return total_distance

# Example usage
distance_matrix = np.array([[0, 10, 15, 20],
                            [10, 0, 35, 25],
                            [15, 35, 0, 30],
                            [20, 25, 30, 0]])

# Solve TSP using nearest neighbor heuristic
tour = nearest_neighbor_tsp(distance_matrix)

# Calculate total distance of the tour
total_distance = calculate_total_distance(tour, distance_matrix)

print("Shortest tour using nearest neighbor heuristic:", tour)
print("Total distance of the tour:", total_distance)
