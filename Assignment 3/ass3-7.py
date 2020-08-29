def summer_69(l):
    sum=0
    len=l.__len__()
    if len == 0:
        return 0
    for i in l:
        if i!=6:
            sum=sum+i
        else:
            break
    for i in range(len):
        if l[i]==9:
            break
    for j in range(i+1,len):
        sum=sum+l[j]
    return sum
        
l=[2,1,6,9,11]
print(summer_69(l))
            