
fib1, fib2 = 0, 1

# Number of terms
n = 10

# Print the first two numbers
print(fib1, fib2, end=" ")

# Generate the next Fibonacci numbers
for _ in range(n - 2):
    next_fib = fib1 + fib2
    print(next_fib, end=" ")
    fib1, fib2 = fib2, next_fib  # Update values
