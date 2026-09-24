#Entrar com um ângulo em graus e imprimir: seno, coseno, tangente, secante, co-secante e co-tangente deste ângulo.

import os
import math
os.system('cls')

angulo = int(input("Digite o angulo: "))
radiano = math.radians(angulo)

seno = math.sin(radiano)
coseno = math.cos(radiano)
tangente = math.tan(radiano)
secante = 1/seno
cosecante = 1/coseno
cotangente = 1/tangente

print("Seno: ", seno)
print("Coseno: ", coseno)
print("Tangente: ", tangente)
print("Secante: ", secante)
print("Cosecante: ", cosecante)
print("Cotangente: ", cotangente)