def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += ((-1) ** (i + 1)) / i
    return sum

n = int(input("Enter a positive integer: "))
print(sum_series(n))