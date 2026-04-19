def generate_combinations(n, current=[]):
    # Base case: if the current list has length n, return it as a result
    if len(current) == n:
        return [current]
    
    # Recursive case: add 0 or 1 and continue
    return (generate_combinations(n, current + [0]) +
            generate_combinations(n, current + [1]))

# Example usage
n = 3
combinations = generate_combinations(n)

# Print all combinations
for combo in combinations:
    print(combo)