# Recursive factorial
def factorial_recursive(n: int) -> int:
    """Return n! using recursion."""
    if not isinstance(n, int):
        raise TypeError("factorial_recursive() requires an integer")
    if n < 0:
        raise ValueError("factorial_recursive() requires a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative factorial
def factorial_iterative(n: int) -> int:
    """Return n! using an iterative approach."""
    if not isinstance(n, int):
        raise TypeError("factorial_iterative() requires an integer")
    if n < 0:
        raise ValueError("factorial_iterative() requires a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_io() -> None:
    """Read an integer from input, print factorials computed iteratively and recursively."""
    try:
        n = int(input("Enter a non-negative integer: ").strip())
        if n < 0:
            print("Invalid input: please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input: please enter an integer.")
        return

    print(f"Iterative: {n}! = {factorial_iterative(n)}")
    print(f"Recursive: {n}! = {factorial_recursive(n)}")

if __name__ == "__main__":
    factorial_io()