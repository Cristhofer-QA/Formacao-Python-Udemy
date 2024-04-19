nome = 'Cristhofer Mian'
altura = 1.81
peso = 92.5
imc = peso / altura ** 2

# f-strings, onde consigo incluir variáveis dentro de strings

linha_1 = f'{nome} tem {altura} m de altura, pesa {peso} kg e seu IMC (com 3 casas decimais) é {imc:.3f}'

print(linha_1)