def is_prime(n):
    """
    Determine if a number is prime.
    
    Args:
        n: An integer to check for primality.
    
    Returns:
        True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


# Example usage
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 10, 11, 20, 29, 97]
    for num in test_numbers:
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
