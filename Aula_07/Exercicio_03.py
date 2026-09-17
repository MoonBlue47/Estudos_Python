#Entrar com vários números positivos e imprimira média dos números digitados.

# Códigos comentados são erros

import os
os.system('cls')

cont = 0
soma = 0

while True:
    numero = int(input("Digite os numeros: "))
    if numero < 0:
        break
    soma = soma + numero   # adicao = numero + soma
    cont = cont + 1        #cont+1

media = soma/cont      #media = adicao/cont
print(f"Resultado: {media}")