a=int(input())
b=int(input())
sum=0
co=0
for i in range(1,a):
    if a%i==0:
        sum+=i
for j in range(1,b):
    if b%j==0:
        co+=j
if sum==b and co==a:
    print('Amicable')
else:
    print('Not Amicable')