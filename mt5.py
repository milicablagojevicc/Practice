def find_divisors(n: int) -> list:
    """
    Returns a list of all divisors of the given integer.

    :param n: The integer to find divisors for.
    :return: A list of divisors of n.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    return [i for i in range(1, n + 1) if n % i == 0]


# User input
if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    divisors = find_divisors(number)
    print(f"Divisors of {number}: {divisors}")