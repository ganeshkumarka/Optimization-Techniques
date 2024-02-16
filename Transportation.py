
import numpy as np

def northwest_corner(cost_matrix, supply, demand):
    m, n = cost_matrix.shape
    allocation = np.zeros((m, n))

    i, j = 0, 0

    while i < m and j < n:
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0:
            i += 1
        else:
            j += 1

    return allocation

#calculating min cost
def calculate_total_cost(allocation, cost_matrix):
    total_cost = np.sum(allocation * cost_matrix)
    return total_cost

# Example problem
cost_matrix = np.array([
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8,3, 3, 2]
])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

# Apply the Northwest Corner Method
allocation = northwest_corner(cost_matrix, supply, demand)
min_cost=calculate_total_cost(allocation, cost_matrix)
# Print the results
print("Allocation Matrix:")
print(allocation)
print("\n\nMinimum cost = ", min_cost)