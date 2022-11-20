#This code will parse a xml document by looking into a specif tag

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
tree= ET.fromstring(response)
data= tree.findall('.//count')

lst=[]
count=0
for i in data:
    total= i.text
    y= int(total)
    lst.append(y)
    count=count+1
    #print(lst)
print('Total:',sum(lst))
print('Count:',count)
