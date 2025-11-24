import math

def is_prime(n: int) -> bool:
    """
    Checks if a given integer n is a prime number.

    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.

    Args:
        n: The integer to check for primality.

    Returns:
        True if n is prime, False otherwise.
    """
    # 1. Handle edge cases: n < 2 (0, 1, negatives)
    if n <= 1:
        return False
    
    # 2. Handle the only even prime number
    if n == 2:
        return True
    
    # 3. Handle all other even numbers (composite)
    if n % 2 == 0:
        return False
    
    # 4. Check for odd divisors from 3 up to the square root of n
    # We only need to check up to the square root because if n has a divisor 
    # greater than its square root, it must also have one less than its square root.
    # We step by 2 (i.e., 3, 5, 7, 9, ...) because we already eliminated even numbers.
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    # If no divisors were found, the number is prime
    return True

# --- Test Cases based on the generated plan ---
TEST_CASES = [
    (17, True),      # Standard Prime
    (4, False),      # Standard Composite
    (2, True),       # Edge Case: Smallest Prime
    (1, False),      # Edge Case: Definition
    (0, False),      # Edge Case: Zero
    (-5, False),     # Edge Case: Negative
    (9, False),      # Composite (Small)
    (101, True),     # Large Prime
    (121, False),    # Composite (Square)
    (3, True),       # Small Prime added for completeness
    (19, True)       # Another standard Prime
]

print("--- Running Prime Checker Test Suite ---")
all_passed = True
for number, expected in TEST_CASES:
    result = is_prime(number)
    status = "PASS" if result == expected else "FAIL"
    
    if status == "FAIL":
        all_passed = False
        
    print(f"Testing n={number:<4}: Expected={expected}, Result={result:<5} -> {status}")

if all_passed:
    print("\n✅ All generated test cases passed successfully.")
else:
    print("\n❌ Some test cases failed.")
