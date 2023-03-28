# Apenas "corrigindo" (nao que estivesse errado) o seu codigo

from random import randint

file = open("vocab.txt", "r+", encoding="utf-8")
lines = file.readlines()
vocabulary = []
a = "none"
file.close()

for line in lines:
    if line.endswith("\n"):
        vocabulary.append(line.strip())

list_size = len(vocabulary)

while a != "exit":

    r = randint(0, list_size)

    line = vocabulary[r]
    words = line.split()
    true_or_false = 0

    while true_or_false == 0:

        # Daqui em diante estou chutando pois nao da pra ver no video
        print(f"Korean: {words[0]}")
        a = input("English: ")
        if a == words[1]:
            print("that's correct! :)")
            true_or_false = 1
        else:
            print("that's wrong :(")
