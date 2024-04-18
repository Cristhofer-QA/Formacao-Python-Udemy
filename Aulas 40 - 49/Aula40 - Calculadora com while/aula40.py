"""
    Calculadora com while
"""
while True:
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')
    operador = input('Digite um operador ( + - * / ) ')
    operadores_permididos = '+-*/'
    
    numeros_validos = None
    
    primeiro_numero_formatado = 0
    segundo_numero_formatado = 0
    
    try:
        primeiro_numero_formatado = float(primeiro_numero)
        segundo_numero_formatado = float(segundo_numero)
        
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue
    
    if operador not in operadores_permididos:
        print('Operador inválido!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    print('Realiando sua conta. Confira o resultado abaixo.')
    
    if operador == '+':
        print(primeiro_numero_formatado + segundo_numero_formatado)
    
    elif operador == '-':
        print(primeiro_numero_formatado - segundo_numero_formatado)
        
    elif operador == '*':
        print(primeiro_numero_formatado * segundo_numero_formatado)
        
    elif operador == '/':
        print(primeiro_numero_formatado / segundo_numero_formatado)
    
    sair = input('Deseja sair? [s]im ou [n]ão. ')
    sair = sair.lower()
    if sair:
        if sair == 's':
            break
        elif sair == 'n':
            continue
        