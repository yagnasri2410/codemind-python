a,b,c=map(int,input().split())
s=(a+b+c)/2
ar=(s*(s-a)*(s-b)*(s-c))
d=ar**(1/2)
print("{:.2f}".format(d))