import os
os.system('cls')

numero = int(input("Digite um numero: "))
cont = 0

while True:
    if numero == 0:
        break
    if numero >= 100 and numero <= 200:
         cont+=1
    numero = int(input("Digite um numero: "))

print(f"Numeros digitados: {cont}")