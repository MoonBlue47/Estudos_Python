#Construir um algoritmo que indique se o número digitado está compreendido entre 20 e 90 ou não. 

import os
os.system('cls')

numero = int(input("Digite um numero: "))

if numero >=20 and numero <=90:
    print("Está no intervalo!")
else: 
    print("Não está no intervalo")