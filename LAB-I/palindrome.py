a = int(input("Enter the Number: "))
temp = a 
rev=0
while (a!=0) :
 r = a%10 
 rev = rev*10 + r 
 a = a//10
  
 if temp==rev : 
     print("Palindrome Number")
 else: 
      print("Not Palindrome Number")
         