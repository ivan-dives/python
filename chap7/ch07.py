prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print letter + 'u' + suffix
	else:
		print letter + suffix


# for count_letters
def find(strng, ch, start=0):
	index = start
	while index < len(strng):
		if strng[index] == ch:
			return index
		index += 1
	return -1

def count_letters(fruit, ch):
	count = 0
	for char in fruit:
		if char == ch:
			count += 1
	print count

def count_letters_2(str, ch):
	count = 0
	for char in str:
		if char == ch:
			find(str, ch, start=0)
			count += 1
	print count


count_letters("Hello world", 'o')
