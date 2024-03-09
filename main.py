import random

def gerar_numero_sorteado():
    return random.randint(1, 100)

def obter_palpite(nome_jogador):
    while True:
        palpite_str = input(f"{nome_jogador}, qual é o seu palpite? ")
        try:
            return int(palpite_str)
        except ValueError:
            print("Por favor, insira um número válido.")

def exibir_mensagem_palpite(palpite, numero_sorteado):
    if palpite < numero_sorteado:
        print("Muito baixo!")
    elif palpite > numero_sorteado:
        print("Muito alto!")

def exibir_palpites(palpites):
    print("Palpites:", end=" ")
    print(*palpites, sep=", ")

def verificar_palpite(palpite, numero_sorteado, palpites, jogador):
    palpites.append(palpite)
    exibir_mensagem_palpite(palpite, numero_sorteado)

    if palpite == numero_sorteado:
        if jogador:
            print(f"UAUU, essa foi certeira. Parabéns!! Você acertou o número {numero_sorteado}")
        else:
            print(f"O computador acertou o número {numero_sorteado}!")
        exibir_palpites(palpites)
        print(f"Total de palpites: {len(palpites)}")
        return True

def fazer_suposicao_computador(palpites, faixa_min, faixa_max):
    palpite_computador = random.randint(faixa_min, faixa_max)
    while palpite_computador in palpites:
        palpite_computador = random.randint(faixa_min, faixa_max)
    print(f"🤖 O computador fez um palpite: {palpite_computador}")
    return palpite_computador

def deseja_jogar_novamente():
    return input("Deseja jogar novamente? (s/n): ").lower() == 's'

def agradecer_jogador(nome_jogador):
    print(f"Obrigado por jogar, {nome_jogador}! Até a próxima. 👋")

def guess_the_number():
    while True:
        numero_sorteado = gerar_numero_sorteado()
        palpites = []
        tentativas_jogador = 0
        tentativas_computador = 0
        faixa_min = 1
        faixa_max = 100

        print("Bem-vindo ao jogo Guess the Number")
        nome_jogador = input("Digite seu nome: ")

        while True:
            palpite = obter_palpite(nome_jogador)
            tentativas_jogador += 1
            if verificar_palpite(palpite, numero_sorteado, palpites, True):
                break
            elif palpite < numero_sorteado:
                faixa_min = palpite + 1
            else:
                faixa_max = palpite - 1

            palpite_computador = fazer_suposicao_computador(palpites, faixa_min, faixa_max)
            tentativas_computador += 1
            if verificar_palpite(palpite_computador, numero_sorteado, palpites, False):
                break

        print(f"Tentativas do jogador: {tentativas_jogador}")
        print(f"Tentativas do computador: {tentativas_computador}")

        if not deseja_jogar_novamente():
            agradecer_jogador(nome_jogador)
            break

guess_the_number()
