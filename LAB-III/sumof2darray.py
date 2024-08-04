def sum_of_2d_arrays(arr1, arr2):
    rows = len(arr1)
    cols = len(arr1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = arr1[i][j] + arr2[i][j]
    return result

array1 = [[1, 2], [3, 4]]
array2 = [[5, 6], [7, 8]]
sum_array = sum_of_2d_arrays(array1, array2)
print("Sum of 2D arrays:", sum_array)
