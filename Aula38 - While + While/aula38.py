quantidade_linhas = 5
quantidade_colunas = 5

linha = 1
coluna = ...

while linha <= quantidade_linhas:
    coluna = 1
    while coluna <= quantidade_colunas:
        print(f'Linha: {linha}. Coluna: {coluna}')
        coluna += 1
    print('*' * 15)
    linha += 1
    