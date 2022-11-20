#finding links and try to open them
import re
import urllib.request, urllib.parse, urllib.error
#lst=[]
url= input('Enter URL:')
fhand=urllib.request.urlopen(url)

for line in fhand:
        line= line.decode().strip()
        #print(line)
        if line.startswith('<li'):
            line= line.split('<a ')
            pos= line[1]
            po= pos.split('>')
            pos2=po[0]
            print(pos)
