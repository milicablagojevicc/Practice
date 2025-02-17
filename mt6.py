def get_multiple_of(n):
    """Prompt the user to enter a multiple of `n` and validate input."""
    while True:
        try:
            user_input = int(input(f"Enter a multiple of {n}: "))
            if user_input % n == 0:
                return user_input
            else:
                print(f"Error: {user_input} is not a multiple of {n}. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Example usage
multiple = get_multiple_of(6)
print(f"You entered: {multiple}")