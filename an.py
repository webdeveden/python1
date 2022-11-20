#languagges

def  greet(lang):
    if lang== 'french':
        print('Bonjour')
        print('English: Hello')
        print('Espanola: Hola')

        #another option

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
