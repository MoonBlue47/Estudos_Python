import os 
os.system('cls')

nomes = []
cont = 0 

while cont < 10:

    digito = input("Digite um nome: ")
    
    nomes.insert(cont, digito)
    
    cont += 1

print("Nomes cadastrados:")
for indice, nome in enumerate(nomes):
    print(f"Nome {indice+1}: {nome}")