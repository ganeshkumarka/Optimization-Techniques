# A bakery sells two types of cakes, chocolate and vanilla. 
# The bakery has a daily budget of 500 dollars and can produce 
# at most 400 cakes per day. Each chocolate cake costs 2 dollars 
# to make and sells for 5 dollars, while each vanilla cake costs 
# 1 dollar to make and sells for 3 dollars. The bakery also has to 
# satisfy the demand of at least 100 chocolate cakes and at least 
# 50 vanilla cakes per day. How many cakes of each type should the 
# bakery make to maximize its revenue? What is the maximum revenue? 
# Implement using linear programming package
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