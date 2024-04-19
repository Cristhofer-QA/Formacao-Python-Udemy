"""
    Fatiamento [i:f:p] [::]
    i - início 
    f - fim (se eu quiser incluir o caractere da posição do fim, devo informar +1). Posso omitir o final 
                ex: variavel[5:], com isso, inicia no índice 5 e vai até o final. O inverso também funciona
    p - passo (de quantos em quantos caracteres, por padrão vai de 1 em 1)
    Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[:5])
print(len(variavel[1:5]))