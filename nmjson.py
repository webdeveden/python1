
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
for item in info:
    y= str(item)
    lst.append(y)
x= lst
for k,v in lst.items():
    print(k,v)
