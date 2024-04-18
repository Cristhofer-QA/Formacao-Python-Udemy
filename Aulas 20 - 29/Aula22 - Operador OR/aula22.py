"""
    Operador OR
    Apenas uma das condições precisam ser TRUE.
    Se um for TRUE, a sentença toda é verdadeira.
    
    AVALIAÇÃO DE CURTO CIRCUITO
        Numa sentença, o python retorna o primeiro valor verdadeiro! Por exemplo:
            print(False or False or 'ABC' ou True)
            Como 'ABC' é diferente dos valores falsy (ver o operador AND), então ele se torna TRUE, logo o pyton retorna-o.
"""

entrada = input('Digite E para "entrar" ou S para "sair": ')
usuario_correto = 'Usuário teste'
senha_correta = 'Teste123'

if entrada == 'E' or entrada == 'e':
    print('Entrar')
    usuario_digitado = input('Digite seu usuário: ')
    senha_digitada = input('Digite sua senha: ')
    if  usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print('Bem vindo ao sistema!')
    else:
        print('Usuário ou senha incorreto!!!!')

elif entrada == 'S':
    print('Adeus!!!!')
    