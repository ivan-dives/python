#
# countletters.py
# 

def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)

with open('alice_in_wonderland.txt') as f:
    text = f.read()

counts = 128 * [0]

for letter in text:
    counts[ord(letter)] += 1

outfile = open('alice_count.dat', 'w')
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

for i in range(len(counts)):
    if counts[i]:
	outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()
