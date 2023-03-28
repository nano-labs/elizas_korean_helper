import random

file = open("vocab.txt", "r+", encoding="utf-8")
read = file.readlines()
mdv = []
line = []
a = "none"

for line in read:
    if line[-1] == '\n':
        mdv.append(line.strip())

listsize = len(mdv)

while a != "exit":

    line = []

    r = random.randint(0, listsize)

    line = mdv[r]
    linestr = line.split()
    trueorfalse = 0

    while trueorfalse == 0:

        # Daqui em diante estou chutando pois nao da pra ver no video
        print(f"Korean: {linestr[0]}")
        a = input("English: ")
        if a == linestr[1]:
            print("that's correct! :)")
            trueorfalse = 1
        else:
            print("that's wrong :(")
