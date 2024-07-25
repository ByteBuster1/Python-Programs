x=int(input("Enter the number: "))
r=0
while x!=0:   
 rem = x%10
 r=rem+r
 x=x//10
print(r)
 