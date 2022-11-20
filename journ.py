#these code will print out the top of something in file
import re

fname= input('Enter file name:')
fh= open(fname)
ln= input('Top number:')
count= dict()
num=0
if fh is None:
    print(fname,'File not found')
for line in fh:
    if line.startswith('From '):
        words= line.split()
        pos= words[1]
        num= num+1
        count[pos]= count.get(pos,0)+1
lst= list()
for k,v in count.items():
    lst.append((v,k)) # double parenthese cz list can't contain more than one item, so we put a list into tuple
lst= sorted(lst,reverse=True)

for k,v in lst[:int(ln)]:# lst[:], look into the list and find the top or last of of a list.
    print(v,':',k)
print('These are top',ln,'of',num,'sent')
#print(lst)
