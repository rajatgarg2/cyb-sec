def spy_gamer(l):
   c=0
   len=l.__len__()
   for i in range(len):
       if l[i]==0:
           c=1
           break
   if c==1:
        
        for j in range(i+1,len):
            if l[j]==0:
                c=2
                break
        if c==2:
            for k in range(j+1,len):
                if l[k]==7:
                    return True
        else:
            return False
   else:
        return False
    
   
l=[1,2,3,0,0,7,5,4]
print(spy_gamer(l))