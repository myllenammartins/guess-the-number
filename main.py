import random

def guess_the_number():

    while True:
        numero_aleatorio = random.randint(1, 100)
        palpite_array = []
        total_palpites = 0

        print("Bem vinda(o) ao jogo Guess the Number")
        nome_jogador = input("Digite seu nome: ")

        while True:
            palpite = int(input(f"{nome_jogador}, qual o seu palpite? "))
            palpite_array.append(palpite)
            total_palpites += 1

            if palpite < numero_aleatorio:
             print("Muito baixo!")
            elif palpite > numero_aleatorio:
                print("Muito alto!")
            else:
                print(f"UAUU, essa foi certeira. Parabéns!! Você acertou o número {numero_aleatorio}")
                print("Palpites:", end=" ")
                for p in palpite_array:
                    print(p, end=" ")
                print()
                print(f"Total de palpites: {total_palpites}")
                break

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            print(f"Obrigado por jogar, {nome_jogador}! Até a próxima.")
            break

guess_the_number()