def almost_there(n):
    if abs(n-100)<=10 or abs(n-200)<=10:
        return True
    else:
        return False

n=int(input('Enter a number : '))
print(almost_there(n))