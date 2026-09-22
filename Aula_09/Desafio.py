import os 
os.system('cls')

def somar():
    total = num01+num02
    print(total)
def subtrair():
    total = num01-num02
    print(total)
def dividir():
    total = num01*num02
    print(total)
def multiplicar():
    total = num01/num02
    print(total)


num01 = int(input("Digite um numero: "))
num02 = int(input("Digite outro numero: "))
op = ""

match op:
    case 1:
        somar()
    case 2:
        subtrair()
    case 3:
        dividir()
    case 4:
        multiplicar()