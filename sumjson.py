
import json
input='''
[
    { "id":"001",
      "x": "2",
      "name": "Chuck"
     } ,
     {"id": "009",
      "x": "7",
      "name": "Eden"
     }
]'''

info= json.loads(input)
print('User count:',len(info))

lst=[]
for items in info:
    y= int(items['x'])
    lst.append(y)
print('sum X:',sum(lst))
