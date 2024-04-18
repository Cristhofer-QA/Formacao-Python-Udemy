"""
    Flag - marcar um local
    None = não valor
    is e is not = é ou não é (tipo, valor, identidade)
    id = Identidade
"""
v1 = 'a'
print(id(v1))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não Faça algo')
    
print(f'O valor de {passou_no_if = }.\n A variável passou_no if é None? {passou_no_if is None}')
print(f'********************\nA variável passou_no if NÃO É None? {passou_no_if is not None}')
