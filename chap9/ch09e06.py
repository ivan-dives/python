# Add your doctest here:
"""
	>>> 13 in junk
	True
	>>> del junk[4]
	>>> junk
	[3, 7, 9, 10, 17, 21, 24, 27]
	>>> del junk[a:b]
	>>> junk
	[3, 7, 27]
	>>> nlist[2][1]
	0
	>>> nlist[0][2]
	17
	>>> nlist[1][1]
	5
	>>> import string
	>>> string.split(message, '??')
	['this', 'and', 'that']

"""

# Write your Python code here:
junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
a = 2
b = 7

nlist = [[0, 1, 17], [0, 5, 0], [0, 0, 0]]

message = 'this??and??that'

if __name__ == '__main__':
	import doctest
	doctest.testmod()
