#Entrar com números enquanto forem positivos e imprimir quantos números foram digitados.

import os
os.system('cls')

numero = int(input("Digite um numero: "))
cont = 0 #Contagem de numeros digitados

while True: 
    if numero < 0:
        break
    numero = int(input("DIgite um numero: "))
    cont+=1
print("Total de numeros digitados ",cont)