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

obj = [-3, -2]
#constraints
#chocolate+vanila<=400
#2*chocolate + 1*vanila<=500
#chocolate>=100
#vanila>=50

lhs_ineq = [[1, 1], [2, 1]] 
rhs_ineq =[400, 500] 
bnd = [(100, 400),(50, 400)] 
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd) 
print("Chocolate cake",int(opt.x[0]))
print("Vanila cake",int(opt.x[1]))
max_profit=sum(c * -x for c, x in zip(obj, opt.x))
print("Maximum profit =",max_profit)