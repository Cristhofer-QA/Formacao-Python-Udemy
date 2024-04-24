"""
    Iterável -> ste, range, etc (objeto que tem o método __iter__)
    Iterador -> quem sabe entregar um valor por vez
    next -> me entregue o próximo valor
    iter -> me entregue seu iterador
"""
texto = 'Cristhofer'  # iterável
iterador = iter(texto)  # iterador

while True: 
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break