a=int(input())
s=a**2
sum=0
for i in str(s):
    sum=sum+int(i)
if sum==a:
    print("Neon Number")
else:
    print("Not Neon Number")
