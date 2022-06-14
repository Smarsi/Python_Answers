'''
Crie uma rotina para a conversão de uma lista de temperaturas. Utilize a lista abaixo 
como exemplo de argumento de entrada para a rotina. Para o último item da lista, crie a 
rotina para a conversão da escala Kelvin para Celsius

'''

# declaração das funções usadas para os cálculos --------------------

def celsius_fahrenheit(temperatura):
    resultado = (( float(temperatura) * 9) / 5) + 32
    return ("%.2f" % resultado)

def fahrenheit_celsius(temperatura):
    resultado = ((float(temperatura) - 32 ) * 5 ) / 9 
    return ("%.2f" % resultado)

def kelvin_celcius(temperatura):
    resultado = float(temperatura) - 273.15 
    return ("%.2f" % resultado) 

def celcius_kelvin(temperatura):
    resultado = float(temperatura) + 273.15 
    return ("%.2f" % resultado) 

def kelvin_fahrenheit(temperatura):
    em_celcius = kelvin_celcius(float(temperatura))
    resultado = celsius_fahrenheit(float(em_celcius))
    return ("%.2f" % float(resultado)) 

def fahrenheit_kelvin(temperatura):
    em_celcius = fahrenheit_celsius(float(temperatura))
    resultado = celcius_kelvin(float(em_celcius))
    return ("%.2f" % float(resultado)) 

# Fim das declarações de função -----------------------------------------------

quantidade = int(input("Quantas temperaturas você irá converter? "))
contador = 1
valores = {}
while contador <= quantidade:
    print("")
    print("")
    print("")
    print("Vamos cadastrar o item "+str(contador)+" de "+str(quantidade))
    valores[str(contador)] = {}

    valores[str(contador)]['temperatura'] = float(input("Digite a temperatura: "))
    valores[str(contador)]['escalaOrigem'] = input("Digite a Escala de origem (C , F ou K): ")
    valores[str(contador)]['escalaDestino'] = input("Digite a Escala de Destino (C , F ou K): ")

    if (valores[str(contador)]['escalaOrigem'] == valores[str(contador)]['escalaDestino']):
        print("ERRO: A escala de origem é igual a escala de destino! Por favor digite novamente ou aperte 'CTRL + C' para interromper o programa.")
    else:
        contador = contador + 1 

print('--------------------------------------------------------------------------------------')
print('   Temperatura  |    Escala de Origem    |    Escala de Destino    |    Resultado     ') #Cabeçalho da tabela

for i in valores:
    origem = valores[i]['escalaOrigem']
    destino = valores[i]['escalaDestino']
    temperatura = valores[i]['temperatura']

    # Verificação para transformação do valor (chamando as funções específicas de cada transformação)
    if origem == 'c' or origem == 'C':
        if destino == 'f' or destino == 'F':
            resultado_final = celsius_fahrenheit(temperatura)
        if destino == 'k' or destino == 'K':
            resultado_final = celcius_kelvin(temperatura)

    if origem == 'f' or origem == 'F':
        if destino == 'c' or destino == 'C':
            resultado_final = fahrenheit_celsius(temperatura)
        if destino == 'k' or destino == 'K':
            resultado_final = fahrenheit_kelvin(temperatura)
        
    if origem == 'k' or origem == 'K':
        if destino == 'c' or destino == 'C':
            resultado_final = kelvin_celcius(temperatura)
        if destino == 'f' or destino == 'F':
            resultado_final = kelvin_fahrenheit(temperatura)

    # Exibindo os itens da tabela final (com os resultados)
    print('     {}        |           {}           |         {}                |        {}       '.format(temperatura, origem, destino, resultado_final))

print('--------------------------------------------------------------------------------------')