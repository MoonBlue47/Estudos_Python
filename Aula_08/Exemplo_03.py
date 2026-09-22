import os 
os.system('cls')

#append() -> adicionar um elemento a minha lista 
#insert() -> insere um elemento em uma posição especifica
#remove() -> remove um elemento da minha lista 
#for -> usado para correr a lista 

lista = ["A", 35, 3.14, True, False, 2026,"Senai"]

lista.remove("Senai")

del lista[2] 

print(lista)


lista.pop(2)
print(lista )