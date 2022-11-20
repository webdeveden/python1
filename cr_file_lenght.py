#this program will only print file with some specific amount of letters
fname= input('Enter file name:')
fh= open(fname)
#ll= input('Number')
ln= fh.read()
# condition
if len(ln) > 1000:
    print('Ooops, too large file')
else:
    print(ln)
