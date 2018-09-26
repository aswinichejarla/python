string1=raw_input()
rev_string=reversed(string1)
if list(string1)==list(rev_string):
    print "yes"
else:
    print "no"
