f=open('intro.txt')
#for line in f:
#    line = line.rstrip()
#    print(line)
#    wds = line.split()
#    print(wds)

inp = f.read().split()
#print(inp)

counts = dict()
words = inp
biggest=0
#print(words)
for word in words:
    counts[word] = counts.get(word,0) +1
    if biggest < counts[word]:
        biggest = counts[word]
        bigword=word
#print(counts)

for aaa,bbb in counts.items():
    print(aaa,bbb)
print(word,biggest)
