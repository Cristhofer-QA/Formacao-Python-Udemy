"""
    while / else
    se por algum motivo o while não for executado completamente (algum break), NÃO executa o else
"""

string = 'Qualquer valor'
i = 0
while i <len(string):
    letra = string[i]
    
    if letra == ' ':
        break
    
    print (letra)
    i += 1
else:
    print (f'Não há espaço na string "{string}"')
print('Fora do while.')

