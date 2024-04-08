from pulp import LpMinimize, LpProblem, LpVariable, lpSum

# Define supply points, demand points, and transportation costs
supply_points = ['S1', 'S2']
demand_points = ['D1', 'D2']
transportation_costs = {
    ('S1', 'D1'): 10, ('S1', 'D2'): 20,
    ('S2', 'D1'): 15, ('S2', 'D2'): 25
}
supply = {'S1': 100, 'S2': 150}
demand = {'D1': 120, 'D2': 130}

# Create a linear programming problem
prob = LpProblem("Transportation Problem", LpMinimize)

# Create decision variables
variables = LpVariable.dicts("Transport", (supply_points, demand_points), lowBound=0, cat='Continuous')

# Add objective function
prob += lpSum(variables[i][j] * transportation_costs[(i, j)] for i in supply_points for j in demand_points)

# Add supply constraints
for i in supply_points:
    prob += lpSum(variables[i][j] for j in demand_points) <= supply[i]

# Add demand constraints
for j in demand_points:
    prob += lpSum(variables[i][j] for i in supply_points) >= demand[j]

# Solve the problem
prob.solve()

# Output the results
print("Optimal Transportation Plan:")
for i in supply_points:
    for j in demand_points:
        if variables[i][j].value() > 0:
            print(f"Transport {variables[i][j].value()} units from {i} to {j}")

print("Total Transportation Cost:", round(prob.objective.value(), 2))
