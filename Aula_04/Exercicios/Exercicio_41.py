#Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.

import os
os.system('cls')

nota01 = float(input("Dgite o numero: "))
nota02 = float(input("Dgite o numero: "))
nota03 = float(input("Dgite o numero: "))
nota04 = float(input("Dgite o numero: "))

media = ((nota01*1)+(nota02*2)+(nota03*3)+(nota04))/10
print(f"Media: {media:.2f}")