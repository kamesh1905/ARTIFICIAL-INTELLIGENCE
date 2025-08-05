
import random

# Objective function
def f(x):
    return -x**2 + 10*x

# Hill Climbing Algorithm
def hill_climb(start_x, step_size=0.1, max_iterations=1000):
    current_x = start_x
    current_value = f(current_x)
    
    for _ in range(max_iterations):
        # Look at neighbors
        next_x1 = current_x + step_size
        next_x2 = current_x - step_size
        
        next_val1 = f(next_x1)
        next_val2 = f(next_x2)
        
        # Find the better neighbor
        if next_val1 > current_value:
            current_x, current_value = next_x1, next_val1
        elif next_val2 > current_value:
            current_x, current_value = next_x2, next_val2
        else:
            # No better neighbors, stop climbing
            break

    return current_x, current_value

# Starting point
start = random.uniform(0, 10)
result_x, result_val = hill_climb(start)

print(f"Start at x = {start:.2f}")
print(f"Peak found at x = {result_x:.2f}, f(x) = {result_val:.2f}")
