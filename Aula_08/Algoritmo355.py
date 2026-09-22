import os 
os.system('cls')

num = []
cont = 0 

while cont < 8:
    digito = int(input("Digite um número: "))
    
    num.insert(cont, digito)
    cont += 1

print("Lista digitada:", num)

for i in num: 
    if i == 0 or i % 6 == 0:
        print(f"O número {i} é múltiplo de 6")
    else:
        print(f"O número {i} não é múltiplo de 6")
