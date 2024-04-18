"""
    Iterando strings com while
"""

nome = 'Cristhofer Mian'
tamanho_nome =  len(nome)
nova_string = ''
contador = 0

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'
    contador += 1
    
print(nova_string)