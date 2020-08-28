def count(s):
    a,b=0,0
    for i in s:
        if(i.islower()):
            a+=1
        elif(i.isupper()):
            b+=1
    return a,b
s=input('Enter a string : ')
a,b=count(s)
print("Upper case letters : ",b,
      "Lower case letters : ",a)