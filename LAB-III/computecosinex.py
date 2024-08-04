import math

def compute_cos(x, n):
    cos_x = 0
    for i in range(n):
        sign = (-1) ** i
        cos_x += sign * (x ** (2 * i)) / math.factorial(2 * i)
    return cos_x

x = float(input("Enter x: "))
n = int(input("Enter the number of terms: "))
print(compute_cos(x, n))