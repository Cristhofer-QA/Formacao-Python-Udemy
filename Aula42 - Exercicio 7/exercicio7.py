"""
    Verificar qual letra apareceu mais na frase.
"""

frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    
    letra_atual = frase [i]
    i +=1
    if letra_atual == ' ':
        continue
    
    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual
    
print(f'A letra que apareceu mais vezes foi {letra_apareceu_mais_vezes}.')
print(f'Apareceu {qtd_apareceu_mais_vezes} ')