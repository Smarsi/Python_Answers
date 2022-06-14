'''
    Crie uma rotina que calcule a soma dos 100 primeiros elementos da séria de
    Fibonacci (0, 1, 1, 2, 3, 5, 8, ...). 

'''


sequencia = [] ##Iniciando a sequencia de Fibonacci 
ultimo = 1
penultimo = 1
sequencia.append(penultimo)
sequencia.append(ultimo)

contador = 3

while contador <= 100:
    numero = ultimo + penultimo
    sequencia.append(numero)
    penultimo = ultimo
    ultimo = numero

    contador = contador + 1

print(sum(sequencia))