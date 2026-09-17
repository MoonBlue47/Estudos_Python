import os
os.system('cls')

acm = 0
cont = 0

numero = int(input("Digite um numero: "))

while True:
    if numero < 0:
        break
    acm = acm + numero
    cont += 1
    numero = int(input("Digite um numero: "))

media = acm/cont
print(f"média de numeros digitados: {media}")