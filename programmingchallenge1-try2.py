# This is my second try for the programming challenge 1
# Idea credits for Stuart Moore
import os

wordobj = open("wordlist.txt", "r+")
wordlist = wordobj.read()
scrambledwords = []
for i in range(10):
    inp = str(input("enter the given words: "))
    scrambledwords.append(inp)

for item in scrambledwords:
    print("\n"+item)

list = wordlist.split('\n')
sortedscram = []
sortedlist = []
for scram in scrambledwords:
    scramb = ''.join(sorted(scram))
    sortedscram.append(scramb)

for scram in list:
    scramb = ''.join(sorted(scram))
    sortedlist.append(scramb)
dictos = {}

for i in range(0, 1276):
    dictos[list[i]] = sortedlist[i]
print()
listofsoles = []

for ss in sortedscram:
    for sc in sortedlist:
        if sc == ss:
            for scrambled, unscrambled in dictos.items():
                if ss == unscrambled:
                    print(scrambled + "  is the solution to %s"%(ss))
                    listofsoles.append(scrambled)

for i in listofsoles:
    print(i+",",sep=' ', end='', flush=True)
