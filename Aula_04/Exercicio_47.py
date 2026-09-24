#Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo: 123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser impresso

import os
import math
os.system('cls')

numero = int(input("Digite um numero de 3 digitos (CDU): "))

c = numero // 100
d = (numero % 100) // 10
u = numero % 10

numero_invertido = (u*100) + (d*10) + c