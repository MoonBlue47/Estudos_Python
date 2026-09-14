#Entrar com um número e imprimir o logaritmo desse número na base 10.

import os
import math
os.system('cls')

numero = int(input("Digite um numero: "))
log = math.log10(numero)

print(f"log de {numero} é {log:.2f}")