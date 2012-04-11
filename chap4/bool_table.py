expression = raw_input("Enter a boolean expression in two variables, p and q: ")

print " p	q	%s" % expression
length = len( " p	q	%s" % expression)
print length*"="

for p in True, False:
	for q in True, False:
		print "%-7s %-7s %-7s" % (p, q, eval(expression))
