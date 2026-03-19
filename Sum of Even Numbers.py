def sum_even_numbers(numbers):
    """Return the sum of all even numbers in a list."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    total = 0

    for num in numbers:
        if num % 2 == 0:
            total = total + num

    return total


print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12
print(sum_even_numbers([1, 3, 5, 7]))         # 0
print(sum_even_numbers([2, 4, 6, 8]))         # 20
print(sum_even_numbers([2, 2, 5, 21, 2005]))  # 4
print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 20