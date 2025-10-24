import random
from colorama import init, Fore, Style
init(autoreset=True)

def jogar():
    print(Fore.CYAN + "Bem-vindo ao Adivinha o Número!")

    # Escolhe dificuldade
    print("Escolhe um nível de dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 50)")
    print("3 - Difícil (1 a 100)")

    nivel = input("Nível (1/2/3): ")
    if nivel == "1":
        max_num = 10
        tentativas = 5
    elif nivel == "2":
        max_num = 50
        tentativas = 7
    elif nivel == "3":
        max_num = 100
        tentativas = 10
    else:
        print(Fore.YELLOW + "Nível inválido, escolhendo Fácil por defeito.")
        max_num = 10
        tentativas = 5

