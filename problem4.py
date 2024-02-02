# A farmer has a field of 60 acres in which he plants two crops, wheat and barley. 
# The farmer has to plant at least 20 acres of wheat and at least 10 acres of barley. 
# has 1200 pounds of fertilizer and 600 pounds of insecticide available. Each acre of 
# wheat requires 20 pounds of fertilizer and 10 pounds of insecticide, while each acre 
# of barley requires 10 pounds of fertilizer and 15 pounds of insecticide. The profit
# from an acre of wheat is 200 dollars, and the profit from an acre of barley is 150 dollars. 
# How many acres of each crop should the farmer plant to maximize his profit? 
# What is the maximum profit? Implement using linear programming package

from scipy.optimize import linprog

obj = [-200, -150] #values for profit function
#constraints
#20*wheat+ 10 * barley <= 1200 (fertilizer constraint)
#10 *wheat + 15*barley <= 600 (insecticide constraint)

lhs_ineq = [[20, 10], [10, 15]] 
rhs_ineq =[1200, 600] 
bnd = [(20, 60),(10, 60)] 
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd) 
print("Wheat acres",int(opt.x[0]))
print("Barley acres",int(opt.x[1]))
max_profit=sum(c * -x for c, x in zip(obj, opt.x))
print("Maximum profit =",max_profit)