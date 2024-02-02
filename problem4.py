# A farmer has a field of 60 acres in which he plants two crops, wheat and barley. 
# The farmer has to plant at least 20 acres of wheat and at least 10 acres of barley. 
# has 1200 pounds of fertilizer and 600 pounds of insecticide available. Each acre of 
# wheat requires 20 pounds of fertilizer and 10 pounds of insecticide, while each acre 
# of barley requires 10 pounds of fertilizer and 15 pounds of insecticide. The profit
# from an acre of wheat is 200 dollars, and the profit from an acre of barley is 150 dollars. 
# How many acres of each crop should the farmer plant to maximize his profit? 
# What is the maximum profit? Implement using linear programming package


from scipy.optimize import linprog

c = [-5, -3] 
A = [[2, 1], [1, 1]] 
b = [500, 400] 

x0_bounds = (100, None) 
x1_bounds = (50, None) 

result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

num_chocolate_cakes = round(result.x[0])
num_vanilla_cakes = round(result.x[1])
max_revenue = -result.fun

print(f"Number of chocolate cakes to make: {num_chocolate_cakes}")
print(f"Number of vanilla cakes to make: {num_vanilla_cakes}")
print(f"Maximum revenue: ${max_revenue}")