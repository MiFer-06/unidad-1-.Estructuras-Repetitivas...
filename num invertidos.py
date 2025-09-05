'''
Número invertido:
    Invierte los dígitos de un número entero.
Suma de pares e impares:
'''

numero = int(input("Ingresa un número entero: "))

numero_str = str(numero)  #Convertimos el número a cadena (str) para poder iterar sus dígitos.
numero_invertido = ""

for digito in numero_str:
    numero_invertido = digito + numero_invertido  # va agregando al inicio.    En cada iteración, agregamos el dígito al inicio de la nueva cadena.

print("Número invertido:", numero_invertido)