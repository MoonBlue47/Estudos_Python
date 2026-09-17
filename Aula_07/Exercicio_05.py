import os
os.system('cls')

notas = {
    'Amanda': 9.0,
    'Ericl': 8.5,
    'Gabriel': 9.7,
    'Rebeca': 10
}

for aluno, nota in notas.items():
    print(f"O aluno {aluno} tirou {nota}")