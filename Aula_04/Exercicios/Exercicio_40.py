#Entrar com dois números inteiros e imprimir a seguinte saída: dividendo divisor: quociente: resto:

import os
os.system('cls')

dividendo = int(input("Digite um numero: "))
divisor = int(input("Digite um numero: "))

quociente = dividendo/divisor
resto = dividendo%divisor

print(f"Divisor {divisor} \nDividendo {dividendo} \nQuociente {quociente} \nResto {resto}")