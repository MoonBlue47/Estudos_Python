import os
os.system('cls')

print("--- Escola Tio Sam de Idiomas ---")
print("Níveis disponíveis: ")
print("1 - Nível I (R$ 51,50)")
print("2 - Nível II (R$ 65,00)")
print("3 - Nível III (R$ 80,00)")
print("4 - Nível IV (R$ 100,00)")
nivel = int(input("Digite seu nivel (1 ao 4): "))

match nivel:
    case 1:
        mensalidade = 51.50
    case 2:
        mensalidade = 65.00
    case 3:
        mensalidade = 80.00
    case 4:
        mensalidade = 100.00

pagamento = int(input("Digite seu dia de pagamento: "))

if (pagamento == 1):
    desconto = mensalidade*0.15
    valorFinal = mensalidade-desconto
    print(f"Desconto de 15%: R${valorFinal:.2f}")

elif (pagamento > 1 and pagamento <= 5):
    desconto = mensalidade*0.10
    valorFinal = mensalidade-desconto
    print(f"Desconto de 10%: R${valorFinal:.2f}")

elif (pagamento > 5 and pagamento <= 10):
    desconto = mensalidade*0.0389
    valorFinal = mensalidade-desconto
    print(f"Desconto de 3.89%: R${valorFinal:.2f}")
