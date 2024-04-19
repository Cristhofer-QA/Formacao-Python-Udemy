"""
    Exercício
    Peça ao usuário para digitar seu nome
    Peça ao usuário para digirar sua idade
    Se nome e idade forem digitados
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
            
    Se nada for digitado em nome ou idade
        Exiba:
            "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_invertido = nome[::-1]

if nome and idade:
    print('*' * 50)
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if " " in nome:
        print('Seu nome possui espaço(s)')
    else:
        print('Seu nome não possui espaços')
    print( f'Seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    print('*' * 50)
else:
    print('Descupe, você deixou campos vazios.')