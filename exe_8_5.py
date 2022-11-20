# looking into lines and find words with some criteria then count them.
fname = input("Enter file name: ")
fh= open(fname)
count=0
for line in fh:
    line= line.rstrip()
    # adding space after "From" to differentiate it with "From:
    if line.startswith('From '):
        line= line.split()
        line= line[1]
        count +=1
        print(line)
# printing the last result
print('There were',count,'lines in the file with From as the first word')
