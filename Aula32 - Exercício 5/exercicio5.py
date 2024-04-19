"""
    Faça um programa que peça ao usuário qpara digitar um número inteiro, 
    informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
    informe que não é um número inteiro.
"""
numero_digitado = input('Digite um número INTEIRO: ')

try:
   numero_inteiro = int(numero_digitado)
   resto_divisao = numero_inteiro % 2
   if resto_divisao == 0:
       print('O número digitado é par.')
   else:
       print('O número digitado é ímpar.')   
except:
    print('O que digitou não é um número inteiro!!!!')



"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
    exiba a saudação apropriada. Ex. Bom dia 0 - 11, Boa tarde 12 - 17 e boa noite 18 - 23.
"""
hora_digitada = input ('Informe a hora atual: ')

if hora_digitada:
    try:
        hora_inteira = int(hora_digitada)
        if hora_inteira >= 0 and hora_inteira <= 11:
            print('Bom dia!!')
        
        elif hora_inteira >= 12 and hora_inteira <= 17:
            print('Boa tarde!!')
        
        elif hora_inteira >= 17 and hora_inteira <= 23:
            print('Boa noite!!')
            
        else: 
            print('Hora inválida!')
        
    except:
        print('Digite APENAS as horas!')
else:
    print('Digite uma hora!')


"""
    Faça um programa que peça o primeiro nome do usuário. 
    Se o nome tiver 4 letrar ou menos, escreva "Seu nome é curto"; 
    se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
    maior que 6 letras, escreva "Seu nome é muito grande".
"""
nome_digitado = input('Insira apenas seu primeiro nome: ')
quantidade_letras = ...

if nome_digitado:

    if (' ' not in nome_digitado):
        
        quantidade_letras = len(nome_digitado)
        
        if  quantidade_letras <= 4:
            print('Seu nome é curso.')
        elif quantidade_letras <= 6:
            print('Seu nome é normal.')
        else:
            print('Seu nome é grande.')
            
    else:
        print ('Digite apenas o primeiro nome!')
else:
    print('Nome não informado!')





