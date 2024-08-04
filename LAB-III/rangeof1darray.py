def find_range(arr):
    return max(arr) - min(arr)

array = [1, 2, 3, 4, 5]
range_value = find_range(array)
print(f"Range of the array: {range_value}")