'''
    Crie rotinas para conversão de temperaturas da escala Celsius (°C) para a escala 
    Fahrenheit (°F) e vice-versa.
    
'''

def celsius_fahrenheit(temperatura):
    resultado = (( temperatura * 9) / 5) + 32
    return ("%.2f" % resultado)

def fahrenheit_celsius(temperatura):
    resultado = ((temperatura - 32 ) * 5 ) / 9 
    return ("%.2f" % resultado)


#Casos de teste:
print(celsius_fahrenheit(26)) #resultado esperado : 78,8
print(celsius_fahrenheit(35)) #resultado esperado : 95
print(fahrenheit_celsius(80)) #resultado esperado : 26,67
print(fahrenheit_celsius(77)) #resultado esperado : 25