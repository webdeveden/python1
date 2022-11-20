#function code

def  greet(lang):
    if lang== 'french':
        print('Bonjour')
    elif lang== 'espanol':
        print('Hola')
    elif lang== 'english':
        print('Hello')
    else:
        print('None')
#greetings in three languages

print('Greetings:')
lang=input('Enter your language:')
greet(lang)
