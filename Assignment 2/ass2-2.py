def check(l,h,n):
    if n>=l and n<=h:
        print('True')
    else:
        print('False')
l,h=int(input('Enter the lower limit : ')),int(input('Enter the higher limit : '))
n=int(input('Enter a number : '))
check(l,h,n)