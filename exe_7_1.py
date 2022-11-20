# Use words.txt as the file name
fname = input("Enter file name: ")
fhandle= open(fname)
#looping
for line in fhandle:
    line= line.rstrip()
    print(line.upper())
