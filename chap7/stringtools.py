def reverse(s):
	"""
		>>> reverse('happy')
		'yppah'
		>>> reverse('Python')
		'nohtyP'
		>>> reverse("")
		''
		>>> reverse("P")
		'P'
	"""
	l = len(s)
	new_word = ''
	while l > 0:
		new_word += s[(l - 1)]
		l -= 1
	return new_word

def mirror(s):
	"""
		>>> mirror("good")
		'gooddoog'
		>>> mirror("yes")
		'yessey'
		>>> mirror('Python')
		'PythonnohtyP'
		>>> mirror("")
		''
		>>> mirror("a")
		'aa'
	"""
	return s+reverse(s)

def remove_letter(letter, strng):
	"""
		>>> remove_letter('a', 'apple')
		'pple'
		>>> remove_letter('a', 'banana')
		'bnn'
		>>> remove_letter('z', 'banana')
		'banana'
		>>> remove_letter('i', 'Mississippi')
		'Msssspp'
	"""
	new_str = ''
	for s in strng:
		if s != letter:
			new_str += s
	
	return new_str

def is_palindrome(s):
	"""
		>>> is_palindrome('abba')
		True
		>>> is_palindrome('abab')
		False
		>>> is_palindrome('tenet')
		True
		>>> is_palindrome('banana')
		False
		>>> is_palindrome('straw warts')
		True
	"""
	if s == reverse(s):
		return True
	else:
		return False

def count(sub, s):
	"""
		>>> count('is', 'Mississippi')
		2
		>>> count('an', 'banana')
		2
		>>> count('ana', 'banana')
		2
		>>> count('nana', 'banana')
		1
		>>> count('nanan', 'banana')
		0
	"""
	sub_len = len(sub)
	str_len = len(s)
	i = 0
	count = 0

	while i < str_len:
		if sub in s[i:sub_len]:
			count += 1
		i += 1
		sub_len += 1
	return count

def remove(sub, s):
	"""
		>>> remove('an', 'banana')
		'bana'
		>>> remove('cyc', 'bicycle')
		'bile'
		>>> remove('iss', 'Mississippi')
		'Missippi'
		>>> remove('egg', 'bicycle')
		'bicycle'
	"""

		


if __name__ == '__main__':
	import doctest
	doctest.testmod()
