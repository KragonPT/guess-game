import random
import os
from colorama import init, Fore, Style

init(autoreset=True)

score_file = "score.txt"

# Ler melhor score existente
if os.path.exists(score_file):
    with open(score_file, "r") as f:
        try:
            best_score = int(f.read().strip())
        except:
            best_score = 0
else:
    best_score = 0

def jogar():
    global best_score
    print(Fore.CYAN + "="*40)
    print(Fore.CYAN + "       🎯 ADIVINHA O NÚMERO 🎯       ")
    print(Fore.CYAN + "="*40)

    if best_score > 0:
        print(Fore.CYAN + f"🏆 Melhor recorde atual: {best_score} tentativas restantes")

    # Escolher dificuldade
    print("\nEscolhe um nível de dificuldade:")
    print(Fore.YELLOW + "1 - Fácil (1 a 10)")
    print(Fore.YELLOW + "2 - Médio (1 a 50)")
    print(Fore.YELLOW + "3 - Difícil (1 a 100)")

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
    max_tentativas = tentativas

    while tentativas > 0:
        vidas_emoji = "🟢" * tentativas + "⚪" * (max_tentativas - tentativas)
        print(Fore.MAGENTA + f"Tentativas restantes: {vidas_emoji}")

        try:
            chute = int(input(Fore.MAGENTA + f"Adivinha o número entre 1 e {max_num}: "))
        except ValueError:
            print(Fore.RED + "Por favor, insere um número válido.")
            continue

        if chute == numero:
            print(Fore.GREEN + Style.BRIGHT + "\n🎉 PARABÉNS! Acertaste! 🎉\n")

            if tentativas > best_score:
                best_score = tentativas
                with open(score_file, "w") as f:
                    f.write(str(best_score))
                print(Fore.CYAN + f"🥇 Novo recorde! Tentativas restantes: {best_score}")
            break
        elif chute < numero:
            print(Fore.BLUE + "💡 Dica: o número é maior!")
        else:
            print(Fore.BLUE + "💡 Dica: o número é menor!")

        tentativas -= 1
        print(Fore.CYAN + "-"*40)

    if tentativas == 0:
        print(Fore.RED + f"💥 Acabaram as tentativas! O número era: {numero}")

# Loop para jogar de novo
while True:
    jogar()
    replay = input(Fore.CYAN + "Queres jogar de novo? (s/n): ").lower()
    if replay != "s":
        print(Fore.CYAN + "Obrigado por jogar! Até à próxima.")
        break

