a,b=map(int,input().split(':'))
h=a*30
m=b*0.5
p=h+m
n=b*6
l=p-n
if l<=0:
    print(360+l)
elif l>180:
    print(360-l)
else:
    print(l)
