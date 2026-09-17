import os
os.system('cls')
import time

numero = int(input("digite um numero: "))

while True:
    if numero == 0:
        break
    numero = int(input("digite um numero: "))
print("fim do loop")