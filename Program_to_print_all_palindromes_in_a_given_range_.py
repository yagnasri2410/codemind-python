a=int(input())
b=int(input())
for i in range(a,b):
    if i%10==i//10 and i<=100:
        print(i,end=' ')
    elif i<10:
        print(i,end=' ')
    elif i%10==i//100 and i>=100:
        print(i,end=' ')