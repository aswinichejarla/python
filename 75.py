ss1=raw_input()
c=len(ss1)
a=list(ss1)
if c%2==0:
    m=c/2 - 1
    a[m]='*'
    a[m+1]='*'
else:
    m=c/2 - 1
    a[m+1]='*'
print "".join(a)
