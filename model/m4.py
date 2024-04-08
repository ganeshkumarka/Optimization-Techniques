import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
    # Step 1: Reduce the cost matrix
    reduced_matrix = cost_matrix - np.min(cost_matrix, axis=0)
    reduced_matrix -= np.min(reduced_matrix, axis=1)[:, np.newaxis]
    
    # Step 2: Find the minimum number of lines
    num_lines = np.sum(reduced_matrix == 0)
    
    while num_lines < len(cost_matrix):
        # Step 3: Cover all zeroes with the minimum number of lines
        row_covered = np.zeros(len(cost_matrix), dtype=bool)
        col_covered = np.zeros(len(cost_matrix), dtype=bool)
        zero_positions = np.argwhere(reduced_matrix == 0)
        
        for i, j in zero_positions:
            if not row_covered[i] and not col_covered[j]:
                row_covered[i] = True
                col_covered[j] = True
        
        # Step 4: Test for optimality
        if np.sum(row_covered) + np.sum(col_covered) == len(cost_matrix):
            break
        
        # Step 5: Modify the cost matrix
        min_uncovered_value = np.min(reduced_matrix[~row_covered][:, ~col_covered])
        reduced_matrix[~row_covered] -= min_uncovered_value
        reduced_matrix[:, col_covered] += min_uncovered_value
    
    # Step 6: Repeat steps 2-5 until an optimal solution is found
    
    # Step 7: Assign tasks to workers
    row_indices, col_indices = linear_sum_assignment(reduced_matrix)
    assignment = np.zeros_like(cost_matrix)
    assignment[row_indices, col_indices] = 1
    
    return assignment

# Example usage
cost_matrix = np.array([[250, 400, 350],
                        [400, 600, 350],
                        [200, 400, 250]])

optimal_assignment = hungarian_algorithm(cost_matrix)
print("Optimal Assignment:")
print(optimal_assignment)
