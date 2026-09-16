import os
os.system('cls')

num01 = 15
num02 = 20
op = "*"

match op:
    case "+":
        total = num01+num02
        print(total)
    case "-":
        total = num01-num02
        print(total)
    case "*":
        total = num01*num02
        print(total)
    case "/":
        total = num01/num02
        print(total)