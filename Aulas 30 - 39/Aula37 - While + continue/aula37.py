"""
    Continue - pula a execução do laço de acordo com uma condição e retorna no início do laço
    Sempre usado para o while que está mais próximo!!!!
"""

contador = 0

while contador < 100:
    contador += 1
    if contador == 6:
        print (f'Não vou mostrar o {contador}!')
        continue
    
    if contador >= 10 and contador <= 40:
        print (f'Não vou mostrar o {contador}')
        continue
    
    print(contador)
    
    if contador == 59:
        break
    
    
    
    



