m=int(raw_input())
a=[]
while(m>0):
    dig=m%10
    a.append(dig)
    m=m//10
print sum(a)
