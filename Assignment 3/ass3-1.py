def isPangram(s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in s:
            return False
    return True

s=input('Enter a string : ')
print(isPangram(s))