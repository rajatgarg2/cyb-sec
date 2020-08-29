def count_primes(n):
    p=0
    for i in range(2,n+1):
        c=0
        for j in range(2,i+1):
            if(i%j==0):
                c+=1
        if c==1:
             p+=1
    return p
                
n=int(input('Enter a number : '))
print(count_primes(n))