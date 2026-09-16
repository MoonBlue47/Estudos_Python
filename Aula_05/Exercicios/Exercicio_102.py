#Entrar com um número e imprimir uma das mensagens: maior do que 20, igual a 20 ou menor do que 20

import os
os.system('cls')

numero = int(input("Digite um numero: "))

if numero > 20:
    print("Maior que 20")
else: 
    print("É menor que 20")