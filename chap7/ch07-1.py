fruit = 'rambutan'
def str_test(fruit="rambutan"):
	"""
	>>> type(fruit)
	<type 'str'>
	>>> len(fruit)
	8
	>>> fruit[:3]
	'ram'
	"""
	
	print type(fruit)
	print len(fruit)
	print fruit[:3]

# str_test()

group = ""
def group_test(group):
	"""
		>>> group = "John, Paul, George, and Ringo"
		>>> group[12:x]
		'George'
		>>> group[n:m]
		'Paul'
		>>> group[:r]
		'John'
		>>> group[s:]
		'Ringo'
	"""
	group = "John, Paul, George, and Ringo"
	x = 18
	group[12:x]
	n = 6
	m = 10
	group[n:m]
	r = 4
	group[:r]
	s = 24
	group[s:]


if __name__ == "__main__":
	import doctest
 	doctest.testmod()
