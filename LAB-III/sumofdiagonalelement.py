def sum_of_diagonal_elements(arr):
    n = len(arr)
    return sum(arr[i][i] for i in range(n))


array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum = sum_of_diagonal_elements(array)
print(f"Sum of diagonal elements: {diagonal_sum}")
