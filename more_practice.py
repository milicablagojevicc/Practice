def add(x, y):
    """Performs addition (trivial but included for clarity)."""
    return x + y

def multiply(a, b):
    """Multiplies a and b using only addition."""
    result = 0
    for _ in range(b):
        result = add(result, a)
    return result

def power(a, b):
    """Computes a**b using only addition (via repeated multiplication)."""
    if b == 0:
        return 1  # Base case: a^0 = 1
    result = a
    for _ in range(b - 1):
        result = multiply(result, a)
    return result

# Read input
a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))

# Compute a**b using only addition
print(f"{a}^{b} =", power(a, b))

#a bit complicated ngl I did not get it