import numpy as np

def vam_initial_solution(supply, demand, costs):
    num_supply = len(supply)
    num_demand = len(demand)
    allocation = np.zeros((num_supply, num_demand))
    
    while np.sum(supply) > 0 and np.sum(demand) > 0:
        penalty_row = []
        penalty_col = []
        
        # Calculate penalty for each row
        for i in range(num_supply):
            row_costs = sorted(costs[i])
            if len(row_costs) >= 2:
                penalty_row.append(abs(row_costs[0] - row_costs[1]))
            else:
                penalty_row.append(0)
        
        # Calculate penalty for each column
        for j in range(num_demand):
            col_costs = sorted(costs[:, j])
            if len(col_costs) >= 2:
                penalty_col.append(abs(col_costs[0] - col_costs[1]))
            else:
                penalty_col.append(0)
        
        # Find the most unbalanced row or column
        max_penalty_row = np.argmax(penalty_row)
        max_penalty_col = np.argmax(penalty_col)
        
        # Find the least cost cell in the most unbalanced row or column
        if penalty_row[max_penalty_row] >= penalty_col[max_penalty_col]:
            least_cost_index = np.argmin(costs[max_penalty_row])
            allocation_amount = min(supply[max_penalty_row], demand[least_cost_index])
            allocation[max_penalty_row, least_cost_index] = allocation_amount
            supply[max_penalty_row] -= allocation_amount
            demand[least_cost_index] -= allocation_amount
            costs[max_penalty_row, :] = np.inf
        else:
            least_cost_index = np.argmin(costs[:, max_penalty_col])
            allocation_amount = min(supply[least_cost_index], demand[max_penalty_col])
            allocation[least_cost_index, max_penalty_col] = allocation_amount
            supply[least_cost_index] -= allocation_amount
            demand[max_penalty_col] -= allocation_amount
            costs[:, max_penalty_col] = np.inf
    
    return allocation

# Example usage
supply = np.array([100, 150, 200])
demand = np.array([120, 130, 170])
costs = np.array([[10, 20, 15], [25, 18, 12], [8, 12, 4]])

initial_solution = vam_initial_solution(supply, demand, costs)
print("Initial Feasible Solution:")
print(initial_solution)
