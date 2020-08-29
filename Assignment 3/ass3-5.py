def has_33(l):
    c=l.__len__()
    for i in range(0,c-1):
        if l[i]==3 and l[i+1]==3:
            return True
    return False

l=[1,3,3]
print(has_33(l))