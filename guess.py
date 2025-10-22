import random
from colorama import init, Fore, Style
init(autoreset=True) # Allow colors back to normal after each print

def jogar():
    print(Fore.CYAN + "Bem-vindo ao Adivinha o Número!")

    # Choose Difficulty
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

    numero = random.randint(1, max_num)

    while tentativas > 0:
        try:
            chute = int(input(Fore.MAGENTA + f"Adivinha o número entre 1 e {max_num}: "))
        except ValueError:
            print(Fore.RED + "Por favor, insere um número válido.")
            continue

        if chute == numero:
            print(Fore.GREEN + "Parabéns! Acertaste!")
            break
        elif chute < numero:
            print(Fore.BLUE + "O número é maior.")
>>>>>>> 8987cab (Add colors and improve game interface)
        else:
            print(Fore.BLUE + "O número é menor.")

        tentativas -= 1
        print(Fore.YELLOW + "Tentativas restantes:", tentativas)

    if tentativas == 0:
        print(Fore.RED + "Acabaram as tentativas! O número era:", numero)

# Loop para jogar de novo
while True:
    jogar()
    replay = input(Fore.CYAN + "Queres jogar de novo? (s/n): ").lower()
    if replay != "s":
        print(Fore.CYAN + "Obrigado por jogar! Até à próxima.")
        break
>>>>>>> 8987cab (Add colors and improve game interface)
