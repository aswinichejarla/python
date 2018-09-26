p=int(raw_input())
count=0
if p>1:
    for i in range(2,p):
        if p%i==0:
            count=count+1
if count>1:
    print "yes"
else:
    print "no"
