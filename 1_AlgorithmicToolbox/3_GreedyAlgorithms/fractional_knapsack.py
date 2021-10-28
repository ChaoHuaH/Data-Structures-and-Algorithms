# A thief finds much more loot than his bag can fit. 
# Help him to find the most valuable combination of items 
# assuming that any fraction of a loot item can be put into his bag.

# Task: to implement an algorithm for the fractional knapsack problem.
# Input Format: 
# |-- The first line of the input contains the number n of items and the capacity W of a knapsack. 
# |-- The next n lines define the values and weights of the items
# |-- The i-th line contains integers vi and wi—the value and the weight of i-th item, respectively
# Constraints: 1 <= n <= 10^3, 0 <= W <= 2*10^6, 0 <= vi <= 2*10^6, 0 <= wi <= 2*10^6  
#              for all 1 <= i <= n, All the numbers are integers.
# Output Format: Output the maximal value of fractions of items that fit into the knapsack. 
# The absolute value of the difference between 
# the answer of your program and the optimal value should be at most 10^(−3). 
# To ensure this, output your answer with at least four digits after the decimal point 
# (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    items = []
    
    # sort the value/weight
    unit_values = [ a / b for a, b in zip(values, weights)]
    sorted_ind = sorted(range(len(unit_values)), key = lambda k: unit_values[k], reverse = True)
    values = [values[i] for i in sorted_ind]
    weights = [weights[i] for i in sorted_ind]
    unit_values = [unit_values[i] for i in sorted_ind]
    # print("unit_values:", unit_values)
    # print("values:", values)
    # print("weights:", weights)

    # put item into knapsack
    for i in range(len(unit_values)):
        if capacity == 0:
            break
        
        a = min(capacity, weights[i])
        # print("===========================")
        # print("capacity:", capacity)
        # print("a:", a)
        value += unit_values[i] * a
        # print("value:", value)
        capacity -= a
        weights[i] -= a
        items.append((values[i], weights[i]))
    
    # print("===========================")
    # print("values:", values)
    # print("weights:", weights)
    # print("item:", items)
    # print("value:", value)

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))