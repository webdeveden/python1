# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input('Enter file name: ')
fh = open(fname)
# No traceback
try:
    fh= open(fname)
except:
    print(fname,'file not found')
#loop
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        line= line[20:]
        count = count+1
        total = total+float(line)
# average
print('Average spam confidence:',total/count)
