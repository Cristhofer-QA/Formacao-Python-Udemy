"""
    Operador NOT
    Usado para inverter expressões
    not True = False
    not False = True
"""

entrada = input('Digite E para "entrar" ou S para "sair": ')
usuario_correto = 'Usuário teste'
senha_correta = 'Teste123'

if entrada == 'E':
    print('Entrar')
    usuario_digitado = input('Digite seu usuário: ')
    senha_digitada = input('Digite sua senha: ')
    if not usuario_digitado or not senha_digitada: # Como o valor vazio é false, aqui to alterando para true para poder entrar na expressão.
        print ('Informe o usuário e senha!!!')
    elif  usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print('Bem vindo ao sistema!')
    else:
        print('Usuário ou senha incorreto!!!!')

elif entrada == 'S':
    print('Adeus!!!!')
