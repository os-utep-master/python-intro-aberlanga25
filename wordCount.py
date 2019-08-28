import sys
import re

input = sys.argv[1]
output = sys.argv[2]

words = []
master = []
counts = []

with open(input, 'r') as inputFile:
    for line in inputFile:

        line = line.strip()
        line = re.sub('[!@#$,".:;]', '', line)
        line = re.sub("[-,']",' ', line)
        word = re.split('[ \t]', line)

        for x in word:
            #x.lower()
            if x != '':
                words.append(x)
    words = [item.lower() for item in words]
    words.sort()
    for i in words:
        if i not in master:
            master.append(i)
    for y in master:
        counts.append(words.count(y))

f = open(output, "w")
n = len(master)
for w in range(n):

    f.write(str(master[w]) + " " +str(counts[w])+"\n")
f.close()


