import math
p,q=map(int,raw_input().split())
c=p * q
if math.sqrt(c).is_integer():
    print "yes"
else:
    print "no"
