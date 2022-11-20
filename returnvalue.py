# Return value

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'eng':
        return 'Hello'
    elif lang == 'fr':
        return 'bonjour'
    else:
        return '"see appendix A"'

#now we can invoke them

print('in spanish we say:', greet('es'))
print('in french we say:', greet('fr'))
print('in english we say:', greet('eng'))
print('For other languages',greet('en'))
