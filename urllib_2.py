import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    line=line.decode().strip()
    print(line)
