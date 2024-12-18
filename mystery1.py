def collatz_for_real_numbers(n, iterations=100):
    count = 0
    while count < iterations:
        print(f"Step {count + 1}: n = {n}")
        
        # Check if n is even (approximately)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        
        # Break if n becomes too small (close to 1 for real numbers)
        if abs(n - 1) < 1e-6:  # Close enough to 1
            print("The number has approximately reached 1.")
            break
        
        count += 1

    if count == iterations:
        print("Reached maximum iterations without converging to 1.")
    return n

# Example usage with any value of n
n = float(input("Enter a number (n): "))  # User input for n
print(f"Starting with n = {n}")
collatz_for_real_numbers(n)