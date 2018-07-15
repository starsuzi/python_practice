str = 'X-DSPM-Confidence: 0.8475'
ipos= str.find(':')
print(ipos)
print(str[18:])
val=float(str[19:])
print(val)

han= open('mbox-short.txt')

for line in han:
    line=line.rstrip()
    wds=line.split()
    if wds[0]!='From':
        continue
    print(wds[2])
