# import numpy as np

# def simplex_method(c, A, b, maximize=True):
#     m, n = A.shape
#     tableau = np.hstack((A, np.eye(m)))
#     tableau = np.hstack((tableau, np.vstack((b, np.zeros((m, 1))))))
#     if maximize:
#         c_bar = -c
#     else:
#         c_bar = c

#     while any(c_bar > 0):
#         entering_var = np.argmax(c_bar)
#         ratios = tableau[:, -1] / tableau[:, entering_var]
#         if all(ratios <= 0):
#             print("Problem is unbounded.")
#             return None, None
#         leaving_var = np.argmin(ratios[ratios > 0])
        
#         pivot = tableau[leaving_var, entering_var]
#         tableau[leaving_var, :] /= pivot
#         for i in range(m + 1):
#             if i != leaving_var:
#                 tableau[i, :] -= tableau[i, entering_var] * tableau[leaving_var, :]
                
#         c_bar -= c_bar[entering_var] * tableau[leaving_var, :n]

#     return tableau[:, -1], tableau[-1, -1] if maximize else -tableau[-1, -1]

# if __name__ == "__main__":
#     # Example input
#     c = np.array([3, 2])     # Coefficients of the objective function
#     A = np.array([[1, 1],    # Coefficients of the constraint matrix
#                   [2, 1]])
#     b = np.array([4, 5])     # Right-hand side vector

#     # Solve linear optimization problem (maximization)
#     solution, optimal_value = simplex_method(c, A, b, maximize=True)
#     print("Maximization:")
#     print("Optimal solution:", solution)
#     print("Optimal value:", optimal_value)

#     # Solve linear optimization problem (minimization)
#     solution, optimal_value = simplex_method(c, A, b, maximize=False)
#     print("\nMinimization:")
#     print("Optimal solution:", solution)
#     print("Optimal value:", optimal_value)

import numpy as np

def simplex(A, b, c):
    # Initialize the tableau
    b = b[:, np.newaxis]
    tableau = np.vstack((np.hstack((A, c)), np.hstack((b, 0))))
    
    # Find the pivot column
    pivot_col = np.argmin(tableau[:-1, -1] / tableau[:-1, :-1])
    
    while np.any(tableau[:-1, -1] < 0):
        # Find the pivot row
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        pivot_row = np.argmin(ratios)
        
        # Perform row operations
        tableau[pivot_row] /= tableau[pivot_row, pivot_col]
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i] -= tableau[pivot_row] * tableau[i, pivot_col]
        
        # Update the pivot column
        pivot_col = np.argmin(tableau[:-1, -1] / tableau[:-1, :-1])
    
    # Extract the solution
    x = tableau[:-1, -1]
    return x

# Problem data
A = np.array([[1, 1], [2, 1]])
b = np.array([10, 15])
c = np.array([-3, -2]) # Note: We use negative coefficients for minimization

# Solve the problem
solution = simplex(A, b, c)
print("Optimal solution:", solution)
