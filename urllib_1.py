import urllib.request, urllib.parse, urllib.error

url=input('Enter URL:')
fhand=urllib.request.urlopen(url)

count=0
for line in fhand:
    line=line.decode().strip()
    count=count+1
    print(line)
print('Sequence Total:',count)
