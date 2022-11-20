#Extracting a web page words and treat it like a File
import urllib.request, urllib.parse, urllib.error

fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts= dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]= counts.get(word,0)+1
#print(counts)
#sorting them ascending
lst=[]
bigword= None
bigcount= -1
for k,v in counts.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
for k,v in lst:
    if bigword is None and k > bigcount:
        bigword= v
        bigcount=k
        print(bigword,':',bigcount)
