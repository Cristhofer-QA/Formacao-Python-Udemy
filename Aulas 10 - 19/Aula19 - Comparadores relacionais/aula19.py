"""
        Operadores de comparação (relacionais)
        >   Maior que       2 > 1
        >=  Maior ou igual  2 >= 2
        <   Menor que       1 < 2
        <=  Menor ou igual  1 <= 5
        ==  Igual           'a' == 'a'
        !=  Diferente       'a' != 'b'
"""

a = 7
b = 7

A = 'A'
B = 'A'

maior = a > b
maior_ou_igual = a >= b
menor = a < b
menor_ou_igual = a <= b
igual = A == B
diferente = A != B

print( f'{a} é maior que {b}?',maior)
print(f'{a} é maior ou igual a {b}?',maior_ou_igual)
print(f'{a} é menor que {b}?',menor)
print(f'{a} é menor ou igual a {b}?',menor_ou_igual)
print(f'{A} é igual a {B}?',igual)
print(f'{A} é diferente de {B}?',diferente)