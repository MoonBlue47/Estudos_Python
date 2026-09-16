#Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e tiver menos que 25 anos, imprimir nome e a mensagem: ACEITA. Caso contrário, imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou F.)

import os
os.system('cls')

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
idade = int(input("Digite sua idade: "))

if sexo == 'f' and idade <= 25:
    print(f"Nome: {nome}, Aceita!")
else:
    print(f"Nome: {nome}, não aceita!")