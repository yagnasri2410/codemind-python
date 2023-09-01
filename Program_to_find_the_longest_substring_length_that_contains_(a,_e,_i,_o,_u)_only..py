string=input()
v=set("aeiou")
m=0
c=0
for char in string:
    if char in v:
        c+=1
    else:
        m=max(m,c)
        c=0
m=max(m,c)
print(m)