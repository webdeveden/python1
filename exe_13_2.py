#This code will parse a xml document by looking into a specif tag

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url:')
response = urllib.request.urlopen(url,context=ctx).read()
print('Retrieving',url)
print('Retrieving', len(response), 'characters')
# parsing the XML document to python
tree= json.loads(response)
data= tree['comments']
#print(data)
lst=[]
count=0
for item in data:
    y= item['count']
    count=count+1
    x= int(y)
    lst.append(x)
print('Count:',count)
print('Sum:', sum(lst))
