m=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(m):
    print "yes"
else:
    print "no"
