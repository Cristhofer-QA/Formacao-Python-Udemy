# String são iteráveis, ou seja, consigo ir de elemento em elemento.
# Por exemplo:
#            indice   0   1  2  3  4  5  6  7  8  9
#            String   C   R  I  S  T  H  O  F  E  R
#   indice negativo  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#

# nome = 'Cristhofer'
# print(nome[0])
# print('tho' in nome)
# print('tho' not in nome)

nome_digitado = input ('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_digitado:
    print(f'{encontrar} está em {nome_digitado}')
else:
    print(f'{encontrar} NÃO está em {nome_digitado}!')  