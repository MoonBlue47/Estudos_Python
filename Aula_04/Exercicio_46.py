#Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o novo saldo, considerando o reajuste de 1%.

import os
import math
os.system('cls')

saldo = int(input("Digite seu salario: "))

reajuste = (saldo*1.01)

print(f"Reajuste: {reajuste}")