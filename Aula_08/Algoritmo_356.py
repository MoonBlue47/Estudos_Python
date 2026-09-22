import os 
os.system('cls')

aluno = []

for i in range(3):
    nomeAluno = input("Digite um nome: ")
    pr1 = float(input("Digite a nota da prova 1: "))
    pr2 = float(input("Digite a nota da prova 2: "))

    media = round((pr1 + pr2) / 2)

    aluno.append([nomeAluno, pr1, pr2, media])

print("--- Lista de Resultados ---")
for dados in aluno:
    aluno_nome = dados[0]
    prova1 = dados[1]
    prova2 = dados[2]
    media_aluno = dados[3]
    
    if media_aluno >= 6:
        print(f"AP | Nome:  {aluno_nome} | Pr1: {prova1} | Pr2: {prova2} | (Média: {media_aluno})|")
    else:
        print(f"RE | Nome:  {aluno_nome} | Pr1: {prova1} | Pr2: {prova2} | (Média: {media_aluno})|")
