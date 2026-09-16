#Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade da pessoa. Não se esqueça de verificar se o ano de nascimento é um ano válido

import os
os.system('cls')

ano_Nascimento = int(input("Digite seu ano de nascimento: "))
ano_Atual = int(input("Digite o ano atual: "))

if (ano_Nascimento > 1965 and ano_Nascimento <= 2020) and (ano_Atual == 2026):
    idade = (ano_Atual-ano_Nascimento)
    print(f"Idade: {idade}")
else:
    print("Ano não valido")