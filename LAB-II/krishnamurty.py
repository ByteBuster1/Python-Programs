x=int(input("Enter the number: "))
temp=x
sum=0
while temp>0:
    f=1
    r=temp%10
    for i in range(1,r+1):
        f=f*i
    sum=sum+f 
    x=int(x/10)
if(sum==x):
    print("Krishnamurty Number")
else:
    print("Not Krishnamurty Number")

    


