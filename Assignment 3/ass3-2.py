def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    if a%2!=0 or b%2!=0:
        if a>b:
            return a
        else:
            return b
        
a=int(input('Enter 1st no. : '))
b=int(input('Enter 2nd no. : '))
print(lesser_of_two_evens(a, b))