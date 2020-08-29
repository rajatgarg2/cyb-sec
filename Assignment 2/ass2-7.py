def isprime(i):
    a="Non Prime"
    b="Prime"
    c=0
    if(i>1):
        if(i==2):
            return b
        for j in range(2,i+1):
            if(i%j==0):
                c+=1
        if c==1:
             return b
        else:
             return a
def LoT(n):
    l=[]
    for i in range(2,n+1):
        t=[i]
        s=isprime(i)
        t.append(s)
        t=tuple(t)
        l.append(t)
    return l
n=int(input('Enter the limit : '))
print(LoT(n))
