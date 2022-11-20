fname= input('Enter file name:')

try:
    fh= open(fname)
except:
    print('File not found')
    quit()
eden= dict()

for lines in fh:
    line= lines.split()
    for words in line:
        eden[words]= eden.get(words,0)+1
bigcount= -1
bigword= None
for a,b in eden.items():
    if b > bigcount:
        bigcount= b
        bigword= a
print(bigword,':',bigcount)
print(eden)
