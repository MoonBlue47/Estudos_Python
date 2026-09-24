# 🐍 Formação Backend Python: Fundamentos

Repositório destinado ao registo, versionamento e consolidação dos exercícios práticos desenvolvidos durante o curso de Backend em Python, cobrindo desde a sintaxe inicial até algoritmos, funções e estruturas de dados fundamentais.

---

## 📌 Sobre o Projeto
Este projeto centraliza o código produzido ao longo do treinamento prático de lógica e fundamentos com a linguagem Python. O objetivo é registrar a evolução contínua, organizar as práticas de sintaxe limpa e servir como guia de referência rápida para estruturas essenciais da linguagem.

---

## 📂 Estrutura de Diretórios
A estrutura do projeto mantém a numeração cronológica dos módulos dentro do diretório principal, garantindo fácil navegação e expansão:

```text
fundamentos-python/
├── README.md
└── 01_fundamentos/
    ├── aula_02/             # Entrada/Saída, tipos de dados e formatação
    │   ├── Exemplo_01.py
    │   ├── Exemplo_02.py
    │   ├── Exemplo_03.py
    │   ├── Exercicio_02.py
    │   ├── Exercicio_03.py
    │   ├── Exercicio_04.py
    │   ├── Exercicio_05.py
    │   ├── Exercicio_06.py
    │   └── Pratica_01.py
    ├── aula_04/             # Operadores matemáticos e módulo math
    │   ├── Exercicio_37.py
    │   ├── Exercicio_38.py
    │   ├── Exercicio_39.py
    │   ├── Exercicio_40.py
    │   ├── Exercicio_41.py
    │   ├── Exercicio_42.py
    │   ├── Exercicio_43.py
    │   ├── Exercicio_44.py
    │   ├── Exercicio_46.py
    │   ├── Exercicio_47.py
    │   └── Exercicio_48.py
    ├── aula_05/             # Estruturas condicionais (if, else)
    │   ├── Exemplo_01_2.py
    │   ├── Exercicio_101.py
    │   ├── Exercicio_102.py
    │   ├── Exercicio_103.py
    │   └── Exercicio_104.py
    ├── aula_06/             # Match/Case e laços de repetição (while)
    │   ├── Desafio.py
    │   ├── Exemplo_03_2.py
    │   ├── Exemplo_04.py
    │   ├── Exemplo_05.py
    │   ├── Exemplo_06.py
    │   ├── Exemplo_07.py
    │   └── Exemplo_08.py
    ├── aula_07/             # Estruturas de repetição avançadas e matrizes
    │   ├── Correção_03.py
    │   ├── Correção_04.py
    │   ├── Correção_06.py
    │   ├── Exemplo_08_2.py
    │   ├── Exercicio_01.py
    │   ├── Exercicio_1.1.py
    │   ├── Exercicio_02_2.py
    │   ├── Exercicio_2.2.py
    │   ├── Exercicio_03_2.py
    │   ├── Exercicio_04_2.py
    │   ├── Exercicio_05_2.py
    │   └── Exercicio_07.py
    ├── aula_08/             # Manipulação de listas e fatiamento
    │   ├── Algoritmo355.py
    │   ├── Algoritmo_353.py
    │   ├── Algoritmo_356.py
    │   ├── Algortimo_354.py
    │   ├── Exemplo_01_3.py
    │   ├── Exemplo_02_2.py
    │   ├── Exemplo_03_3.py
    │   ├── Exemplo_04_2.py
    │   └── Exemplo_06_2.py
    └── aula_09/             # Dicionários, tuplas e funções (def)
        ├── Algoritimo459.py
        ├── Algoritimo460.py
        ├── Algoritimo461.py
        ├── CorreçãoD.py
        ├── Desafio_2.py
        ├── Exemplo_01_4.py
        ├── Exemplo_02_3.py
        ├── Exemplo_03_4.py
        ├── Exemplo_04_3.py
        └── Exemplo_05_2.py
````
---

# 📚 Conteúdo Programático & Módulos
| Módulo / Pasta | Tópicos Centrais | Habilidades Desenvolvidas |
| :--- | :--- | :--- |
| aula_02 | Entrada/Saída e Sintaxe | Impressão formatada (`print`, f-strings), caracteres de escape (`\n`, `\t`), verificação de tipos (`type`) e leitura de dados com `input()` |
| aula_04 | Operações e Módulo Math | Cálculos aritméticos, divisão e resto, médias ponderadas, conversões trigonométricas (Tomada de decisão simples e composta (if, else), operadores lógicos (and, or) e validação de intervalos numéricos.sin`, `cos`, `tan`), logaritmos e decomposição numérica. |
| aula_05 | Estruturas Condicionais | Tomada de decisão simples e composta (`if`, `else`), operadores lógicos (`and`, `or`) e validação de intervalos numéricos. |
| aula_06 | Pattern Matching e Repetição | Utilização de `match/case`, laços `while`, paragem manual com `break`, contadores e controlo de tempo de execução com `time.sleep()`. |
| aula_07 | Repetições Indeterminadas e Matrizes | Repetições com valores de paragem (flags), matrizes bidimensionais com laços `for` aninhados, list comprehensions e dicionários. |
| aula_08 | Coleções e Listas | Manipulação avançada de listas (`append`, `insert`, `remove`, `pop`, `del`), iteração com `enumerate()`, listas aninhadas e fatiamento (slicing). |
| aula_09 | Dicionários, Tuplas e Funções | Mapeamentos chave-valor em dicionários, estruturas imutáveis (tuplas), declaração de funções (`def`), retorno de valores e modularização. |

---

# Destaque dos Desafios
## Desafio 01: Escola Tio Sam de Idiomas (`aula_06/Desafio.py`)
* **Objetivo:** Calcular o valor com desconto da mensalidade de um estudante de acordo com a sua opção de nível e o dia em que o pagamento foi efetuado.
* **Técnicas:** Mapeamento de escolhas através de `match/case`, verificação de datas com blocos `if/elif` e formatação de saída financeira com `f-strings`.

## Algoritmo 356: Gestão de Notas com Listas Aninhadas (`aula_08/Algoritmo_356.py`)
* **Objetivo:** Registar notas de provas de vários alunos numa estrutura bidimensional e apresentar um boletim indicando a situação de aprovação ou reprovação
* **Técnicas:** Iteração controlada por `range()`, listas aninhadas (matrizes de dados) e arredondamento numérico com `round()`.

## Desafio 2: Calculadora Modularizada com Funções (`aula_09/Desafio_2.py`)
* **Objetivo:** Criar um menu interativo de operações matemáticas modularizado através de funções personalizadas em Python.
* **Técnicas:** Declaração de funções com def, direcionamento de execução via match/case e reutilização de código.

---

# Pré-requisitos
* **Python versão 3.10** ou superior instalada (necessário para o suporte ao match/case).
* Terminal de comandos ou IDE da sua preferência (VS Code, PyCharm).
