def f(n):
	return 3*n - 6

def g(n):
	return 5*n + 2

def h(n):
	return -2*n + 17

def doto(value, func):
	return func(value)

print doto(7, f)
print doto(7, g)
print doto(7, h)
