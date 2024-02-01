# Fractional Knapsack Implementation

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def fractional_knapsack(items, capacity):
    # Calculating the value-to-weight ratios for each item
    value_weight_ratio = [(item[0] / item[1], item[0], item[1]) for item in items]

    # Sorting the items using quicksort based on value-to-weight ratios
    value_weight_ratio = quicksort(value_weight_ratio)

    max_value = 0  # Maximum value that can be obtained
    knapsack = [] 

    for ratio, value, weight in value_weight_ratio:
        if capacity == 0:
            break

        fraction = min(1, capacity / weight)
        value_in_knapsack = fraction * value
        max_value += value_in_knapsack 
        capacity -= fraction * weight
        knapsack.append((value_in_knapsack, weight, fraction))

    return max_value, knapsack

# Example:
items = [(5,5), (2,4), (2,6), (4,2), (5,1)]
capacity = 12
max_value, knapsack = fractional_knapsack(items, capacity)

print("Maximum value:", max_value)
print("Items in the knapsack:")
for value, weight, fraction in knapsack:
    print(f"Value: {value}, Weight: {weight}, Fraction: {fraction}")





# Testing the program with various problem instances

import random

# Generating random instances
def generate_random_instance(n):
    items = [(random.randint(1, 100), random.randint(1, 50)) for _ in range(n)]
    capacity = random.randint(1, 100)
    return items, capacity

# Testing the program 
for i in range(3):
    items, capacity = generate_random_instance(5)
    print(f"Random Instance {i+1}:")
    print("Items:", items)
    print("Capacity:", capacity)
    max_value, knapsack = fractional_knapsack(items, capacity)
    print("Maximum value:", max_value)
    print("Items in the knapsack:")
    for value, weight, fraction in knapsack:
        print(f"Value: {value}, Weight: {weight}, Fraction: {fraction}")
    print()




