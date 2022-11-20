#printing thre top of something
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count= dict()

for line in fh:
    if line.startswith('From '):
        word= line.split()
        pos= word[5]
        ln= pos.split(':')
        w= ln[0]
        count[w]= count.get(w,0)+1
        #print(w)
lst= list()
for k,v in count.items():
    lst.append((k,v))
lst= sorted(lst)
for k,v in lst:
    print(k,v)
