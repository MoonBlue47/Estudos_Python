import os
os.system('cls')
import time

numero = int(input("Digite um numero para a tabuada: "))
cont = 0

while cont<11:
    total = numero * cont
    print(f"{numero}X{cont}={total}")
    time.sleep(1)
    cont+=1