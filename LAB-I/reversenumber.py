num = int(input("Enter a number "))

num1 = num
sum = 0
while num1 != 0:
  digit = num1 % 10
  sum = (sum*10)+digit
  num1 = num1 // 10

print(f"Reverse of {num} is {sum}")