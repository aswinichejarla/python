m=int(raw_input())
pro=1
while m>0:
    dig=m%10
    pro=pro*dig
    m=m/10
print pro
