from three_lines import *

def nine_lines():
	three_lines()
	three_lines()
	three_lines()

def clear_screen():
	print
	nine_lines()
	nine_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()

def cat_n_times(s, n):
	print s + '\n' * n
