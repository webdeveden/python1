#looking into the file for the mail sender with many emails sent
name = input("Enter file:")
#if len(name) < 1:
    #name= 'mbox-short.txt'
handle = open(name)
ddd= dict()
for line in handle:
    if line.startswith('From '):
        line= line.split()
        #print(line)
        pos= line[1]
        ddd[pos]= ddd.get(pos,0)+1

largest= -1
theword= None
for word,count in ddd.items():
    if count > largest:
        largest= count
        theword= word
    print(theword,largest)
