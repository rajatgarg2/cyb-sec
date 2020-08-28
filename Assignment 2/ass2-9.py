import sys
def fibo(n):
    a,b,c=0,1,1
    while c<=n:
        print(a)
        a,b=b,a+b
        c+=1
fibo(int(sys.argv[1]))