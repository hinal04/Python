# Iterative method to print Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Print first 10 numbers
fibonacci(5) # Output: 0 1 1 2 3 5 8 13 21 34
