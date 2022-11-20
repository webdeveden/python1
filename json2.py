
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
for items in info:
    print('Name:',items['name'])
    print('ID:',items['id'])
    print('Attribute:', items['x'])
    #print(sum(items['x']))
