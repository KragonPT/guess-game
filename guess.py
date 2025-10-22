import random

def play():
    number = random.randint (1, 10)
    trys = 3

    while trys > 0:
        guess = int(input("Adivinha o numero ente 1 e 10: "))

        if guess == number:
           print("Parabéns! Acertaste!")
           return
        elif guess < number:
           print("o numero é maior")
        else:
           print("o numero é menor")

        trys -= 1
        print(" tentantivas restantes", trys)

    print("Perdeste! O numero era: ", number)
if __name__=="__main__":
   play()
