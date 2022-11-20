# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL :')
if len(url)<1:
    url= 'http://py4e-data.dr-chuck.net/known_by_Lusiana.html'
#Word's position
position = int(input('Enter the link position: '))

#to repeat desired times usiing while loop
n= int(input('loop times:'))
while n>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    n= n-1
    count = 0
    for tag in tags:
        count = count +1
        #print(tag)
        #stopping at desired position
        if count>position:
            break
        url= tag.get('href',None)
        lname= tag.contents[0]
    print(url)
    #print(lname)
#print(count)
