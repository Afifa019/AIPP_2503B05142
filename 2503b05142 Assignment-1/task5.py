def find_max(numbers: list[float]) -> float:
    """Return the largest number in a non-empty list of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("find_max() requires a list")
    if not numbers:
        raise ValueError("find_max() requires a non-empty list")
    max_val = numbers[0]
    for x in numbers[1:]:
        if x > max_val:
            max_val = x
    return max_val

def find_max_io() -> None:
    """Read a list of numbers from keyboard, print the largest, and return nothing."""
    s = input("Enter numbers separated by spaces or commas: ").strip()
    if not s:
        print("No input provided.")
        return
    import re
    parts = [p for p in re.split(r"[,\s]+", s) if p != ""]
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        print("Invalid input: please enter only numbers separated by spaces or commas.")
        return
    try:
        largest = find_max(nums)
    except ValueError as e:
        print(e)
        return
    # Print as int when the number is an integer value
    if largest.is_integer():
        print(f"Largest number: {int(largest)}")
    else:
        print(f"Largest number: {largest}")

if __name__ == "__main__":
    find_max_io()