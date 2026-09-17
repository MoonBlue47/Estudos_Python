import os
os.system('cls')

numero = int(input("Digite um numero: "))

while True:
    if numero == -999:
        break
    total = numero*3
    print(total)
    numero = int(input("Digite um numero: "))