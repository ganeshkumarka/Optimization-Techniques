import numpy as np

def create_tableau(c, A, b):
    m, n = A.shape
    tableau = np.zeros((m + 1, m + n + 1))
    tableau[:-1, :-1] = A
    tableau[:-1, -1] = b
    tableau[-1, :n] = c
    return tableau

def select_entering_variable(tableau):
    return np.argmax(tableau[-1, :-1])

def select_leaving_variable(tableau, entering_variable):
    ratios = tableau[:-1, -1] / tableau[:-1, entering_variable]
    return np.argmin(ratios)

def pivot(tableau, key_row, key_col):
    m, n = tableau.shape
    key_element = tableau[key_row, key_col]
    tableau[key_row, :] /= key_element
    for i in range(m):
        if i == key_row:
            continue
        multiplier = tableau[i, key_col]
        tableau[i, :] -= multiplier * tableau[key_row, :]
    return tableau

def is_optimal(tableau):
    return all(x <= 0 for x in tableau[-1, :-1])

def extract_solution(tableau):
    m, n = tableau.shape
    solution = np.zeros(n - 1)
    basic_variables = np.argmax(tableau[:, :-1], axis=1)
    for i, j in enumerate(basic_variables):
        solution[j] = tableau[i, -1]
    return solution

def simplex(c, A, b):
    tableau = create_tableau(c, A, b)
    while not is_optimal(tableau):
        key_col = select_entering_variable(tableau)
        key_row = select_leaving_variable(tableau, key_col)
        tableau = pivot(tableau, key_row, key_col)
    solution = extract_solution(tableau)
    return solution

def main():
    num_variables = int(input("Enter the number of variables: "))
    num_constraints = int(input("Enter the number of constraints: "))

    c = [float(input(f"Enter coefficient for variable x{i+1} in the objective function: ")) for i in range(num_variables)]

    A = np.zeros((num_constraints,num_variables))
    print("Enter the coefficients of the constrained equation")
    for i in range(num_constraints):
            A[i] = [np.array([float(input(f"enter coeficient for xi+1 for constraoined equation xj+1 "))]) for i in range(num_variables)]


    b = [float(input(f"Enter the right-hand side of constraint equation {i+1}: ")) for i in range(num_constraints)]

    solution = simplex(c, A, b)
    print("Optimal solution:", solution)

if __name__ == "__main__":
    main()