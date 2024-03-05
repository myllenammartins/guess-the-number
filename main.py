import random

def gerar_numero_aleatorio():
    return random.randint(1, 100)

def obter_palpite(nome_jogador):
    return int(input(f"{nome_jogador}, qual o seu palpite? "))

def verificar_palpite(palpite, numero_aleatorio, palpite_array):
    palpite_array.append(palpite)

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
        print(f"Total de palpites: {len(palpite_array)}")
        return True

def deseja_jogar_novamente():
    return input("Deseja jogar novamente? (s/n): ").lower() == 's'

def agradecer_jogador(nome_jogador):
    print(f"Obrigado por jogar, {nome_jogador}! Até a próxima.")

def guess_the_number():
    while True:
        numero_aleatorio = gerar_numero_aleatorio()
        palpite_array = []

        print("Bem vinda(o) ao jogo Guess the Number")
        nome_jogador = input("Digite seu nome: ")

        while True:
            palpite = obter_palpite(nome_jogador)
            acertou = verificar_palpite(palpite, numero_aleatorio, palpite_array)
            if acertou:
                break

        if not deseja_jogar_novamente():
            agradecer_jogador(nome_jogador)
            break

guess_the_number()