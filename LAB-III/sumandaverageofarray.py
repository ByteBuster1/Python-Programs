def calculate_sum_and_average(arr):
    total = sum(arr)
    average = total / len(arr)
    return total, average

array = [1, 2, 3, 4, 5]
total, average = calculate_sum_and_average(array)
print(f"Sum: {total}, Average: {average}")