#Lists , tuples , sets , dictionaries
#1.The following is a list of 10 students ages:
# List of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# I. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
# II. Add the min age and the max age again to the list
ages.extend([min_age, max_age])
# III. Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]
# IV. Find the average age
average_age = sum(ages) / len(ages)
# V. Find the range of the ages
age_range = max_age - min_age
# VI. Compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")
print(f"Ages after adding min and max again: {ages}")
print(f"Median age: {median_age}")
print(f"Average age: {average_age}")
print(f"Range of ages: {age_range}")
print(f"Difference between min and average age: {min_avg_diff}")
print(f"Difference between max and average age: {max_avg_diff}")