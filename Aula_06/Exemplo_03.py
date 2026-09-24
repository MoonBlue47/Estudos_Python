import os
os.system('cls')

num01 = 15
num02 = 20
op = "-" #Descide a operação

if op == "+":
    total = num01+num02
    print(total)
elif op == "-":
    total = num01-num02
    print(total)
elif op == "*":
    total = num01*num02
    print(total)
elif op == "/":
    total = num01/num02
    print(total)
elif op == "ex":
    total = num01**num02
    print(total)