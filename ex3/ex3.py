'''
Assumindo um edifício com 10 andares e 4 apartamentos por andar, crie uma rotina 
que apresente o número que deve ser colocado na porta de cada apartamento do edifício. 
Considere que esta rotina também será utilizada em prédios com diferentes números de 
andares e apartamentos por andar. 

'''

# ATENÇÃO: PARA EXECUÇÃO DESTE EXERCÍCIO ESTOU DESCONSIDERANDO O TÉRREO (CONTABILIZANDO APARTAMENTOS APENAS A PARTIR DO 1º ANDAR)

def numeros_apartamentos(andares, apt_por_andar): #recebe o numero de andares e o numero de apartamentos por andar respectivamente
    
    if(apt_por_andar < 10):
        multiplicador = 10
    if(apt_por_andar >= 10):
        multiplicador = 100
    if(apt_por_andar > 100):
        multiplicador = 1000
    if(apt_por_andar > 1000):
        multiplicador = 10000


    resultados = {}
    contador = 1
    while contador <= andares:
        c = 1
        apts = [(contador * multiplicador)+1]
        while c < apt_por_andar:
            last_apt = apts[-1]
            apts.append(last_apt+1)
            c = c + 1
        resultados[str(contador)+'º Andar'] = apts

        contador = contador + 1
    
    return resultados



print(numeros_apartamentos(10, 4))
print(numeros_apartamentos(10, 10))
#print(numeros_apartamentos(60, 30))