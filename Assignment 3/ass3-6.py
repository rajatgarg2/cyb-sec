def blackjack(a,b,c):
    sum=a+b+c
    if a==11 or b==11 or c == 11:
        sum=sum-10
    if sum<=21:
        return sum
    else:
        return "BUST"
    
print(blackjack(9,9,11))
   