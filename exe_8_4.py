#looking into each line and add a word missed
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
# No traceback(but it doesn't work)
try:
    if fname == '.txt':
            fh= open(fname)
except:
    print('Not such file')
    quit()
#checking into list
for line in fh:
    lines=line.split()
    for word in lines:
        if word not in lst:
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)
