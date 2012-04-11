#
# countletters.py
# 

with open('alice_in_wonderland.txt') as f:
    counts = {}

    for letter in f.read():
        try:
            counts[letter] += 1
        except: # letter not in counts
            counts[letter] = 1

printable = { '\n' : 'LF', '\r' : 'CR', ' ' : 'SPACE' }

with open('alice_count.dat', 'w') as f:
    f.write("%-12s%s\n" % ("Character", "Count"))
    f.write("=================\n")
    for letter in sorted(counts):
        f.write("%-12s%d\n" % (printable.get(letter, letter), counts[letter]))

