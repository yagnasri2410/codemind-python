a=int(input())
sum=0
prod=1
for i in str(a):
    sum=sum+int(i)
    prod=prod*int(i)
if sum==prod:
    print("Spy Number")
else:
    print("Not Spy Number")