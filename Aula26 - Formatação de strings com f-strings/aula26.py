"""
    Formatação básica de strings
    s - string
    d - int
    f - float
    .<numero de dígitos>f (quantidade de dígitos após a vírgula)
    x ou X - hexadecimal
    (Caractere) (><^)(quantidade)
    > - esquerda
    < - direita
    ^ - centro
    = - força o sinal de positivo ficar depois dos zeros à esquerda
    sinal - + ou -
    conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')  # À esquerda, quero preencher com espaços em branco até chegar em 10 caracteres
print(f'{variavel: <10}.')  # À esquerda, quero preencher com espaços em branco até chegar em 10 caracteres
print(f'{variavel: ^10}.')  # Centralidanzo, quero preencher com espaços em branco até chegar em 10 caracteres
print(f'{185999.00000 :.1f}')  # 1 casa decimal
print(f'{185999.00000 :,.1f}')  # Inclui uma vírgula como separador de milhar
print(f'{185999.00000 :+,.1f}')  # Inclui um sinal de + em frente ao número positivo
print(f'{-185999.00000 :0=+15,.1f}')  # Inclui zeros à esquerda até chegar a 15 caracteres e inclui um sinal de positivo antes dos zeros
print(f'O hexadecimal de 1500522 é {1500522:08X}')  # hexagecimal com 8 caracteres
