"""
    Repetição.
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True
contador = 0

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    contador = contador + 1
    if contador == 2:
        break
print ('Fim da execução!')