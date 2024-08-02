y=int(input())

if(y%400==0 or (y%100!=0 and y%4==0)):
   print("leap century")
else:
   print("not leap")