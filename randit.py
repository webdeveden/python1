
import random


name= input('Enter your name:')
for code in name:
    code= random.randint(200000,1000000)
print('code:',code)