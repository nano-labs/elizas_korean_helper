#!/usr/bin/env python

# Vamos gameficar um pouco
# Vou manter o codigo estruturado so com algumas funcoes pra ficar simples

from datetime import datetime
from random import choice

from signal import signal, SIGINT
from sys import exit
from time import time


correct_count = 0
questions = 0
start_time = time()


def show_score():
    """Calculate and show your total score."""
    total_time = time() - start_time
    # score eh uma unidade arbitraria. Aumenta com o numero de respostas corretas, com o total de
    # perguntas e diminui com o tempo gasto para tesponder
    score = int((correct_count / total_time) * questions * 10000)
    print(f"\n\n\tYou got {correct_count} out of {questions}!")
    print(f"\tYour score is {score}!")
    score_board(score)


def score_board(current_score):
    """Show the score board."""
    try:
        with open("scoreboard.txt", "r") as board:
            scores = [l.split() for l in board.read().split("\n") if l]
    except FileNotFoundError:
        scores = []

    with open("scoreboard.txt", "a") as board:
        now = datetime.now()
        board.write(f"{int(now.timestamp())} {current_score}\n")

    scores = sorted(scores, reverse=True, key=lambda x: x[1])
    is_worse = True

    print("\n########## SCORE BOARD ##########")
    for timestamp, score in scores:
        date_time = datetime.fromtimestamp(int(timestamp)).strftime("%H:%M:%S %d/%m/%Y")
        if current_score >= int(score) and is_worse:
            is_worse = False
            print(f"--> {now.strftime('%H:%M:%S %d/%m/%Y')}: {current_score}")
        print(f"    {date_time}: {score}")

    if is_worse:
        print(f"--> {now.strftime('%H:%M:%S %d/%m/%Y')}: {current_score}")


def exit_gracefully(*args):
    """Close the programe gracefully."""
    global questions
    questions -= 1
    show_score()
    print('Bye!')
    exit(0)


signal(SIGINT, exit_gracefully)


def run():
    global correct_count
    global questions
    with open("vocab.txt", "r", encoding="utf-8") as file:
        vocabulary = [l.split() for l in file.read().split("\n") if l]

    while True:
        questions += 1
        word, translation = choice(vocabulary)

        if choice([True, False]):
            # aleatoriamente inverte pra perguntar em ingles ou coreano, como tinha sugerido
            word, translation = translation, word

        correct_answer = False

        while not correct_answer:

            print(f"Word: {word}")
            answer = input("Translation: ")
            if answer == translation:
                print("that's correct! :)")
                correct_answer = True
                correct_count += 1
            else:
                print("that's wrong :(")


if __name__ == "__main__":
    run()

exit_gracefully()
