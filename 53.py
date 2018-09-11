m=int(raw_input())
a=[]
while(n>0):
    dig=n%10
    a.append(dig)
    m=m//10
print sum(a)
