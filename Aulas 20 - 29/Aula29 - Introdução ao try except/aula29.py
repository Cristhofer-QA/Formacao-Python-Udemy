"""
    try - tente executar o código
    except - ocorreu algum erro ao executar
"""
numero_str = input('Vou dobrar o número que você digitar: ')


try:
    numero_convertido = float(numero_str)
    print(f'O dobro do número {numero_convertido} é {numero_convertido * 2}')

except:
    print('Digite um número!!!!')