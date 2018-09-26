p=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(p):
    print "yes"
else:
    print "no"
