# this program will extract different content from a txt file
import re

fname= input('File name:')
if len(fname)< 1:
    fname='mbox-short.txt'
fh= open(fname)
ddd= dict()
count=0
#lst= list()
for line in fh:
    line= line.rstrip()
    stuff= re.findall('^From (.\S+@\S+)', line)
    #print(stuff)
    for line in stuff:
        if len(stuff)>0 and line in ddd:
            count= count+1
            ddd[line]=ddd[line]+1
        else:
            ddd[line]= 1
        #print(ddd[line])
lst=[]
for k,v in ddd.items():
    lst.append((v,k))
list= sorted(lst,reverse=True)
for k,v in list:
    print(v,':',k)
print(count)
