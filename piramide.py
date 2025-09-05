'''  Pirámide de asteriscos:
    Dibuja una pirámide de altura n.
'''

piramide = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, piramide + 1):
    espacio = piramide - i
    asteriscos = 2 * i - 1
    print(" " * espacio + "*" * asteriscos)
