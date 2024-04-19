a = 'A'
b = 'B'
c = 1.1

formato_sem_falar_indice = 'a={}, b={}, c={:.2f}'.format(a, b, c)  # Isso fará com que pegue na ordem que as chaves vão aparecendo.
print(formato_sem_falar_indice)

formato_falando_indice = 'a={0}, c={2}, b={1}, c={2}'.format(a, b, c)  # Informando o indice, consigo utilizar os valores em qualquer ordem.
print(formato_falando_indice)

formato_com_parametro_nomeado = 'a={}, b={}, c={nome3:.5f}'.format(a, b, nome3 = c)  #  Nesse exemplo, eu nomeei o parâmetro c. Com isso, todos os outros argumentos que 
print(formato_com_parametro_nomeado)                                                 #  virão após o c, deverão ser nomeados também.