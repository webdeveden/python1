# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_1362864.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
import re
lst=[]
count=0
tags = soup('span')
for tag in tags:
    count=count+1
    tag= tag.contents[0] #finding number characters inside that tag
    x=int(tag)
    lst.append(x)
print(sum(lst))
print(count)
