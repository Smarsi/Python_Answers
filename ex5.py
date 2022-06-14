import re

def Verifica_Validade(data):
    data_atual = 2011 #poderia pegar a data atual ou receber como parametro da função
    data = int(data)

    if data >= data_atual:
        return "Valido"
    else:
        return "Vencido"

def Identificador(numero_identificador):
    bancos = [['2', 'kappa'], ['85', '86', 'omicron'], ['88', 'iota'], ['72', '76', 'kappa'], ['75', 'sigma']]

    for banco in bancos:
        tamanho_verificador = len(banco[0])

        if((re.findall(r"\d{"+str(tamanho_verificador)+"}", numero_identificador)[0]) == banco[0] or (re.findall(r"\d{"+str(tamanho_verificador)+"}", numero_identificador)[0]) == banco[1]):
            return banco[-1]


def Tratamento_Cartao(serial):
    
    quebra = serial.split("=")
    data_expircacao = re.findall(r"\d{4}", quebra[1])[0]
    pan = quebra[0]
    identificador_banco = re.findall(r"\d{6}", (pan.split(";")[1])  )[0]

    nome_banco = Identificador(identificador_banco)
    valido = Verifica_Validade(data_expircacao)

    dados_cartao = {
        "cartao"+ serial: {
            "nome_banco": nome_banco,
            "identificador_banco": identificador_banco,
            "data_expiracao": data_expircacao,
            "valido?": valido,            
            "codigo_pan": pan
        }
    }
    
    return (dados_cartao)



cartao1 = ";854922420655947=20087011490683843?"
cartao2 = ";722792821249=190220153666234?"
cartao3 = ";8657607910110=2209701507597562?"
cartao4 = ";6034523459017=24032012187993726?"
cartao5 = ";83407977524115=2010701164703842?"
cartao6 = ";22554987787910=1903201221224791?"
cartao7 = ";7621767951747=21112018460506111?"
cartao8 = ";24478927568913=230470179307259?"
cartao9 = ";88674481889649=19062014166695784?"
cartao10 = ";76985229117350=1805701127970335?"
cartao11 = ";2147686439882=2712701977197697?"
cartao12 = ";86392841965929=2108201878359745?"

print(Tratamento_Cartao(cartao1))
print(Tratamento_Cartao(cartao2))
print(Tratamento_Cartao(cartao3))
print(Tratamento_Cartao(cartao4))
print(Tratamento_Cartao(cartao5))
print(Tratamento_Cartao(cartao6))
print(Tratamento_Cartao(cartao7))
print(Tratamento_Cartao(cartao8))
print(Tratamento_Cartao(cartao9))
print(Tratamento_Cartao(cartao10))
print(Tratamento_Cartao(cartao11))
print(Tratamento_Cartao(cartao12))