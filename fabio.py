#!/usr/bin/env python

# Como eu faria
from random import choice  # retorna um valor aleatorio de uma lista

# Opcional pra fechar o programa gracefully ao usar Ctrl+C, por exemplo
from signal import signal, SIGINT  # para capturar um Signal Interrupt
from sys import exit  # Pra encerrar o programa


def exit_gracefully(*args):
    """Close the programe gracefully."""
    print('Bye!')
    exit(0)


signal(SIGINT, exit_gracefully)  # Chama exit_gracefully() antes de fechar


def run():
    # "open" pode ser usado como ContextManager entao usando "with" garante que o arquivo vai ser
    # fechado no fim do bloco ou em caso de erro
    with open("vocab.txt", "r", encoding="utf-8") as file:
        # "readlines" eh normalmente preferivel a "read" pois readlines eh um generator e coloca apenas
        # uma linha do arquivo na memoria por vez mas nesse caso, como estamos lendo o aquivo inteiro
        # pra memoria de todo o jeito entao "read" faz mais sentido.
        # Aqui estou matando um monte de coelhos em uma cajadada:
        # 1- usar read().split("\n") me da o mesmo que "readlines()" mas ja limpa os "\n" do final
        # 2- linhas em branco no arquivo serao string vazias entao o "if l" nesse list comprehension
        #    ja limpa essas strings vazias
        # 3- ja quebra cada linha em coreano e ingles
        # 4- com isso ja leio o arquivo, removo o lixo, quebro a linha e crio a variavel um uma so linha
        vocabulary = [l.split() for l in file.read().split("\n") if l]

    # use Ctrl+C ou encerre o script pra fechar
    while True:  # Nao da pra ver sua logica para fechar o programa entao o meu vai rodar pra sempre
        korean, english = choice(
            vocabulary
        )  # retorn um item aleatorio e ja "unpack" em duas variaveis
        correct_answer = False

        while not correct_answer:

            # Daqui em diante estou chutando pois nao da pra ver no video
            print(f"Korean: {korean}")
            answer = input("English: ")
            if answer == english:
                print("that's correct! :)")
                correct_answer = True
            else:
                print("that's wrong :(")


if __name__ == "__main__":
    # Da uma olhada em https://docs.python.org/3/library/__main__.html#idiomatic-usage
    run()

exit_gracefully()
