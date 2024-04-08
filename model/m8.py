#Develop a program to solve an integer linear programming problem where some or 
#all decision variables can only take integer values. This might involve using 
#branch-and-bound techniques or specialized libraries depending on the chosen programming language.

from pulp import LpMaximize, LpProblem, LpVariable

# Create an ILP problem
prob = LpProblem("Integer Linear Programming Problem", LpMaximize)

# Define decision variables
x = LpVariable("x", lowBound=0, cat='Integer')  # Integer variable
y = LpVariable("y", lowBound=0, cat='Integer')  # Integer variable

# Set objective function
prob += 3 * x + 2 * y  # Maximize 3x + 2y

# Add constraints
prob += 2 * x + y <= 8  # Constraint 1: 2x + y <= 8
prob += x + 2 * y <= 10  # Constraint 2: x + 2y <= 10

# Solve the problem
prob.solve()

# Print the results
print("Status:", prob.status)
print("Optimal Solution:")
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Optimal Objective Value:", prob.objective.value())
