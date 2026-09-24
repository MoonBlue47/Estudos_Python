# Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e calcule. Imprima: O valor em reais de cada quilowatt O valor em reais a ser pago O novo valor a ser pago por essa residência com um desconto de 10%

import os
import math
os.system('cls')

salario_minimo = float(input("Digite o valor do sálario mínimo: R$ "))
kw_gastos = float(input("Digite a quantidade de quilowatts gasta: "))

valor_kw = (salario_minimo/7)/100
valor_total = valor_kw*kw_gastos
valor_com_desconto = valor_total*0.90

print(f"Valor de cada quilowatt: R$ {valor_kw:.2f}")
print(f"Valor a sre pago: R$ {valor_total:.2f}")
print(f"Valor com 10% de desconto: R$ {valor_com_desconto:.2f}")