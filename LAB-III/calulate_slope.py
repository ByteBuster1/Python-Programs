def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'Undefined slope'
    return (y2 - y1) / (x2 - x1)

a=int(input("Enter the value of x1: "))
b=int(input("Enter the value of y1: "))
c=int(input("Enter the value of x2: "))
d=int(input("Enter the value of y2: "))

print(calculate_slope(a,b,c,d))