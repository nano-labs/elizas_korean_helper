# Voce esta usando apenas "randint" desse modulo enato importe apenas o metodo que vai usar
import random

# r+ eh para updating. Como voce esta apenas lendo o arquivo melhor usar apenas "r"
# (economiza um buffer)
# Tambem nunca se esqueca de fechar o arquivo. Deixar arquivos abertos pode facilmente levar a um
# "Too Many Open Files" e o linux/unix/bds basicamente morre. Nao sei num windows
file = open("vocab.txt", "r", encoding="utf-8")
# "ducks goes quack": "read" eh uma lista entao deveria ser um nome no plural.
# Tambem eh melhor evitar homonimos. Acredito que tenha usado "read" como passado, "lido" mas 
# "read" tambem significa "ler" entao deixa o nome dessa variavel ambiguo
read = file.readlines()
mdv = []  # nao sei o que "mdv" significa.
# "ducks goes quack": "line" eh singular entao nao deveria ser uma lista.
# De qualquer forma voce nao precisa declarar variavies em python :)
line = []
# Acredito que "a" seja the "answer", certo? Evite variaveis com nomes enigmaticos
a = "none"

# "Is not because you could that you should". Python permite mudar o tipo das variaveis mas nao eh
# por que voce pode que voce deve. Anteriormente voce declarou "line" como uma lista e agora esta
# transformando em string. Tente manter a variavel com o mesmo tipo
for line in read:
    # frequentemente arquivos tem uma ultima linha em branco entao ao ler essa linha esse [-1]
    # possivelmente causara um OutOfRange error.
    # De preferencia use aspas duplas mas mais importante que isso,seja consistente: Use o mesmo
    # tipo de aspas em todo canto
    if line[-1] == '\n':
        mdv.append(line.strip())

# Python code style (PEP 8) sugere usar snake_case pro nome das variaveis
listsize = len(mdv)

while a != "exit":

    line = []  # o mesmo que antes. Nao precisa declarar a variavel e evite mudar o tipo

    r = random.randint(0, listsize)

    line = mdv[r]
    # o nome esta induzindo ao erro. "linestr" nao eh uma string e sim uma lista
    linestr = line.split()
    trueorfalse = 0  # snake_case. Acredito que isso seja uma flag, certo? Melhor usar True/False

    while trueorfalse == 0:

        # Daqui em diante estou chutando pois nao da pra ver no video
        # Estou supondo que linestr eh uma lista com ["palavra em coreano", "palavra em ingles"]
        print(f"Korean: {linestr[0]}")
        a = input("English: ")
        if a == linestr[1]:
            print("that's correct! :)")
            trueorfalse = 1
        else:
            print("that's wrong :(")
