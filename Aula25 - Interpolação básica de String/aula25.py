"""
    Basicamente o mesmo que o Format
    %s      -   para string
    %d e %i -   para int
    %f      -   para float (para formatar a quantidade de casas decimais %.2f, no caso para duas casas decimais)
    %x e %X -   para hexadecimal (ABCDEF0123456789) (para preencher com zeros a esquerda, %04x, que vai incluir zeros à esquerda até ter 4 caracteres)
"""
nome = 'Cristofer'
preco = 1000.5987455
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)