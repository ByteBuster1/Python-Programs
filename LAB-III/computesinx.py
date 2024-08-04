import math

def compute_sin(x, n):
    sin_x = 0
    for i in range(n):
        sign = (-1) ** i
        sin_x += sign * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return sin_x

x = float(input("Enter x: "))
n = int(input("Enter the number of terms: "))
print(compute_sin(x, n))