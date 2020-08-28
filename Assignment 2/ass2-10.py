n=int(input('Enter the size : '))
for i in range(n):
    m=1
    for j in range(i):
        print(m,end=" ")
        m=m*(i-j)//(j+1)
    print("1")