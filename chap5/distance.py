def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2

	result = dsquared**0.5
	
# 	print "dx is ", dx
# 	print "dy is ", dy
# 	print "dsquared is: ", dsquared

	return result

def area(radius):
	return 3.14159 * radius**2

def area2(xc, yc, xp, yp):
	# radius = distance(xc, yc, xp, yp)
	# result = area(radius)
	# return result
	return area(distance(xc, yc, xp, yp))
