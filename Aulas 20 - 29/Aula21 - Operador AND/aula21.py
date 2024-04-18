""" 
    Operador AND
    Todas as condições precisam ser TRUE
    São considerados falsy (visto até agora) ->      0 0.0 '' False
    
    AVALIAÇÃO DE CURTO CIRCUITO
        Numa sentença, o python retorna o primeiro valor false! Por exemplo:
            print(True and 0 and True)
            Como 0 é um valor falsy, então o python retorna-o
""" 

entrada = input('Digite E para "entrar" ou S para "sair": ')
usuario_correto = 'Usuário teste'
senha_correta = 'Teste123'

if entrada == 'E':
    print('Entrar')
    usuario_digitado = input('Digite seu usuário: ')
    senha_digitada = input('Digite sua senha: ')
    if  usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print('Bem vindo ao sistema!')
    else:
        print('Usuário ou senha incorreto!!!!')

elif entrada == 'S':
    print('Adeus!!!!')
