#
# countletters.py
# 

with open('alice_in_wonderland.txt') as f:
    text = f.read()

counts = {}

for letter in text:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1

printable = { '\n' : 'LF', '\r' : 'CR', ' ' : 'SPACE' }

with open('alice_count.dat', 'w') as f:
    f.write("%-12s%s\n" % ("Character", "Count"))
    f.write("=================\n")
    for letter in sorted(counts):
        f.write("%-12s%d\n" % (printable.get(letter, letter), counts[letter]))

