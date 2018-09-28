r=int(raw_input())
count=0
if r>0:
    for i in range(1,r+1):
        if r%i==0:
            print i,
