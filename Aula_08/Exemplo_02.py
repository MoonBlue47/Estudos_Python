import os 
os.system('cls')

#append() -> adicionar um elemento a minha lista 
#insert() -> insere um elemento em uma posição especifica
#remove() -> remove um elemento da minha lista 
#for -> usado para correr a lista 

lista = ["A", 35, 3.14, True]
lista[0] = False
lista[3] = input("Digite um nome de aluno")
lista.insert(4, 2026)

print(lista)