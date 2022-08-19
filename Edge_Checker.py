a,b=map(int,input().split())
p=a-b
if p==1 or p==-1:
    print("Yes")
elif p==9 or p==-9:
    print("Yes")
else:
    print("No")