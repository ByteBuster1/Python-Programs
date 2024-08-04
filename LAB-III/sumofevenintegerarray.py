def sum_of_even_numbers(arr):
    return sum(x for x in arr if x % 2 == 0)

array = [1, 2, 3, 4, 5]
even_sum = sum_of_even_numbers(array)
print(f"Sum of even numbers: {even_sum}")
