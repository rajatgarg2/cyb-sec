def unique(l):
    u=[]
    for i in l:
        if i not in u:
            u.append(i)
    return u
l=[1,2,3,4,5,4,3,2,1]
u=unique(l)
print(u)