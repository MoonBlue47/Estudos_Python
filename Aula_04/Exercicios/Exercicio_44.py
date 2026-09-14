#Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo.

import os
import math
os.system('cls')

numero = float(input("Digite o numero: "))
base = float(input("Digite a base do logaritimo: "))

resultado = math.log(numero, base)

print(f"O logaritimo de {numero} na base {base} é: {resultado}")