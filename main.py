import random

def guess_the_number():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    palpite = None

    while palpite != numero_aleatorio:
        palpite = int(input("Adivinhe o número entre 1 e 100. Qual o seu palpite? "))
        tentativas += 1

        if palpite < numero_aleatorio:
            print("Tente um número maior")
        elif palpite > numero_aleatorio:
            print("Tente um número menor")
        else:
            print(f"UAUU, essa foi certeira. Parabéns!! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")

guess_the_number()