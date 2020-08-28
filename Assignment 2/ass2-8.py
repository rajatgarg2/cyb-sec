def isprime(i):
    a="Non Prime"
    b="Prime"
    if(i>1):
        if(i==2):
            return b
        for j in range(2,i):
            if(i%j==0):
                return a
            else:
                return b
def LoT(n):
    d={}
    for i in range(2,n+1):
        s=isprime(i)
        d[i]=s
    return d
n=int(input('Enter the limit : '))
d=LoT(n)
print(d)
l=[]
for key,values in d.items():
    if values=="Non Prime":
        l.append(key)
for i in l:
    del d[i]
c=0
for key in d.keys():
    c+=1
print("Count of prime key-value pairs : ",c)
    
