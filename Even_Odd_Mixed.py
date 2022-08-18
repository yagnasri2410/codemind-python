n=int(input())
u=n%2
t=n//10
p=t%2
h=n//100
q=h%2
if u==0 and p==0 and q==0:
    print("Even")
elif u!=0 and p!=0 and q!=0:
    print("Odd")
else:
    print("Mixed")
