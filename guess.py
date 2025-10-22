import random

def jogar():
    numero = random.randint (1, 10)
    tentativas = 3

    while tentativas > 0:
        chute = int(input("Adivinha o numero ente 1 e 10: "))

        if chute == numero:
           print("Parabéns! Acertaste!")
           return
        elif chute < numero:
           print("o numero é maior")
        else:
           print("o numero é menor")

        tentativas -= 1
        print(" tentantivas restantes", tentativas)

    print("Perdeste! O numero era: ", numero)
if __name__=="__main__":
   jogar()
