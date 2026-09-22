import os 
os.system('cls')

#append() -> adicionar um elemento a minha lista 
#insert() -> insere um elemento em uma posição especifica
#remove() -> remove um elemento da minha lista 
#for -> usado para correr a lista 

lista = ["A", 35, 3.14, True]
print(lista)

qtde_posicoes = len(lista)
print(qtde_posicoes)

ultimo = lista[-2]
print(ultimo)

item = lista[1]
print(item)

while True: 
    nome = input("Digite um nome ou 0 para encerrar:")
    if nome == "sair": 
        break 

    lista.append(nome)
print(lista)    


for l in lista: 
    print(f"Elemento {l}")