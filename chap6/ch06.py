def is_prime(n):
	"""
	>>> is_prime(2)
	True
	>>> is_prime(3)
	True
	>>> is_prime(7)
	True
	>>> is_prime(5)
	True
	>>> is_prime(6)
	False
	"""

	state = 0		# initially we think that the given number is prime
	i = 2			# shift to 2 because any number is divided by 1
	while i < n:		# or i <= (n - 1)
		if state == 1:
			pass
		elif n == 2:
			state = 1
		elif n % i == 0:
			state = 1 
		i += 1
	
	if state == 0:
		return True
	else:
		return False

def num_digits(n):
	"""
	>> num_digits(12345)
	5
	>>> num_digits(0)
	1
	>>> num_digits(-12345)
	5
	"""

	if n == 0:
		return 1
	count = 0
	while n:
		count = count + 1
		n = n / 10
		if n == -1:
			n = False
	return count

def num_even_digits(n):
	"""
	>>> num_even_digits(123456)
	3
	>>> num_even_digits(2468)
	4
	>>> num_even_digits(1357)
	0
	>>> num_even_digits(2)
	1
	>>> num_even_digits(20)
	2
	"""
	
	count = 0
	while n:
		rest = n % 10
		if rest % 2 == 0:
			count += 1
		n /= 10
	return count
		
def print_digits(n):
	"""
		>>> print_digits(13789)
		9 8 7 3 1
		>>> print_digits(39874613)
		3 1 6 4 7 8 9 3
		>>> print_digits(213141)
		1 4 1 3 1 2
	"""
	while n:
		last = n % 10
		print last,
		n /= 10

def sum_of_squares_of_digits(n):
	"""
		>>> sum_of_squares_of_digits(1)
		1
		>>> sum_of_squares_of_digits(9)
		81
		>>> sum_of_squares_of_digits(11)
		2
		>>> sum_of_squares_of_digits(121)
		6
		>>> sum_of_squares_of_digits(987)
		194
	"""
	
	count = 0
	result = 0
	while n:
		last = n % 10
		result += last**2
		n /= 10
	return result

if __name__ == '__main__':
	import doctest
	doctest.testmod()
