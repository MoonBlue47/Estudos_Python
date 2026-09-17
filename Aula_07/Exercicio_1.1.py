import os
os.system('cls')

while True:
    numero = int(input("Digite um numero: "))
    if numero == -999:
        break
    total = numero*3
    print(total)
print("Fim")