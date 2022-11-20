# Use these code to search for any desired word in a file
count = 0
total = 0
fname = input('Enter file name: ')
fh = open(fname)
# No traceback
try:
    fh= open(fname)
except:
    print(fname, 'file not found')
    quit()
# Searching into a file
inp= input('Enter word:')
for line in fh:
    if inp in line:
        line= line.rstrip()
        count= count+1
        print(line)

print( 'Total:',count)
