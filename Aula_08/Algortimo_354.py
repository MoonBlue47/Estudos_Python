import os 
os.system('cls')

num = []
cont = 0

while cont < 3:
    digite = int(input("Digite um numero: "))
    num.append(digite) 
    cont += 1

print("--- Resultado ---")
print("Números digitados:", num)

for n in num:
    if n % 2 == 0:
        print(f"número {n} é Par")
    else: 
        print(f"número {n} é Ímpar")