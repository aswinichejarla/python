m=raw_input()
"""if all(c in '01' for c in m):
    print "yes"
else:
    print "no"
    """
if not(m.translate(None,'01')):
    print "yes"
else:
    print "no"
