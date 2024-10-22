def max_product(arr):
    if len(arr) < 2:
        return None

    arr.sort()
    return arr[-1] * arr[-2]

# Example usage
print(max_product([1, 5, 3, 9, 2]))  # Output: 45
