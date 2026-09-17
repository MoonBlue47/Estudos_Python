#Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caractere de cada nome

import os
os.system('cls')

nome  = input("DIgite um nome")

while True:
    if nome == "fim":
        break
    print(nome[0]) #posição da letra na palavra
    nome  = input("DIgite um nome")