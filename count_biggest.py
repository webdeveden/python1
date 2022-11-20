#counting the biggest letter and display the bigword and how many time it occured
nam= input('Enter file name:')
fh=open(nam)
counts= dict()
# looking for word and counts times it appears
for words in fh:
    word= words.split()
    for line in word:
        #counts[line]= counts.get(line,0)+1
        #or
        if line in counts:
            counts[line]=counts[line]+1
        else:
            counts[line]=1
#bigword and bigcount
bigcount= None
bigword= None
#looking for  the bigcount and bigword
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount=count
        bigword=word
print(bigword,':',bigcount)
