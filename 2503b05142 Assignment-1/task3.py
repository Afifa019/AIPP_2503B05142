# Function to reverse a string
def reverse_string(s: str) -> str:
    """Return a new string which is the reverse of s."""
    if not isinstance(s, str):
        raise TypeError("reverse_string() requires a string")
    return s[::-1]

def reverse_string_io() -> str:
    """Read a string from input, print its reverse, and return it."""
    s = input("Enter a string: ")
    rev = reverse_string(s)
    print(f"Reversed string: {rev}")
    return rev

if __name__ == "__main__":
    reverse_string_io()