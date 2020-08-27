def palin(s):
    if s==s[ : :-1]:
        return True
    else:
        return False
s=input('Enter a string : ')
print('The string is palindrome : ',palin(s))
