from colorama import Fore
from colorama import Style
from actions import clean_terminal
import time
from banner import *


def personality_quiz():
    clean_terminal()
    personality_quiz_banner()

    # Definindo as perguntas
    perguntas = [
        "VOCÊ GOSTA DE SE AVENTURAR EM NOVAS ATIVIDADES?",
        "VOCÊ SE CONSIDERA UMA PESSOA EXTROVERTIDA?",
        "VOCÊ SE PREOCUPA MUITO COM O QUE OS OUTROS PENSAM DE VOCÊ?",
        "VOCÊ TENDE A PLANEJAR SUAS ATIVIDADES COM ANTECEDÊNCIA?",
        "VOCÊ SE SENTE CONFORTÁVEL EM SITUAÇÕES SOCIAIS?",
        "VOCÊ É UMA PESSOA ORGANIZADA?",
        "VOCÊ GOSTA DE ASSUMIR RISCOS?",
        "VOCÊ COSTUMA SE ESTRESSAR FACILMENTE?",
        "VOCÊ SE CONSIDERA UMA PESSOA CRIATIVA?",
        "VOCÊ TEM DIFICULDADE EM ACEITAR OPINIÕES CONTRÁRIAS AS SUAS?",
    ]

    # Criando uma lista para armazenar as respostas
    respostas = []

    # Loop para fazer as perguntas
    for pergunta in perguntas:
        resposta = ""
        while True:
            resposta = input(
                f"{Fore.CYAN} {pergunta} {Fore.YELLOW} ➀{Fore.CYAN} SIM /{Fore.YELLOW} ➁ {Fore.CYAN}NÃO: {Fore.CYAN} ➤  {Fore.YELLOW}"
            ).lower()

            if resposta != "1" and resposta != "2":
                print(
                    f"{Fore.RED} ✖ POR FAVOR, RESPONDA COM '1 PARA SIM' OU '2 PARA NÃO'. {Style.RESET_ALL}"
                )
                time.sleep(1)
            else:
                break

        # Armazenando a resposta na lista
        respostas.append(int(resposta))

    clean_terminal()

    fishIcon = {
        "TILÁPIA": "𓆛",
        "BARBELA": "𓆜",
        "SALMONETE": "𓆝",
        "PEIXE FOCINHO DE ELEFANTE": "𓆞",
        "PETROCEPHALUS BANE": "𓆟",
        "BAIACU": "𓆡",
    }
    fishCharacteristics = [
        "MUITO POPULAR E COM FACILIDADE EM FAZER NOVOS AMIGOS",
        "TEM UMA PERSONALIDADE POPULAR PORÉM GOSTA DE SER SELETIVO COM SUAS AMIZADES",
        "TEM UM PERSONALIDADE AMIGÁVEL E BONS HÁBITOS DE LIMPEZA",
        "TEM UMA PERSONALIDADE PACÍFICA E NÃO É BOM EM FAZER AMIZADES",
        "TEM UMA PERSONALIDADE INTENSA E BEM TERRITORIALISTA",
        "TEM UMA PERSONALIDADE PACÍFICA, MAS QUANDO AMEAÇADO, PODE SE TORNAR TERRITORIAL E DEFENSIVO",
    ]

    fishProfiles = {
        "TILÁPIA": [1, 1, 2, 2, 1, 2, 1, 2, 1, 1],
        "BARBELA": [1, 1, 2, 1, 1, 1, 2, 1, 1, 1],
        "SALMONETE": [1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
        "PEIXE FOCINHO DE ELEFANTE": [2, 2, 1, 1, 2, 1, 2, 1, 1, 1],
        "PETROCEPHALUS BANE": [2, 1, 1, 2, 2, 1, 2, 1, 1, 1],
        "BAIACU": [1, 1, 2, 1, 1, 1, 2, 2, 1, 2],
    }

    fishNames = [
        "TILÁPIA",
        "BARBELA",
        "SALMONETE",
        "PEIXE FOCINHO DE ELEFANTE",
        "PETROCEPHALUS BANE",
        "BAIACU",
    ]

    fishAffinity = [0, 0, 0, 0, 0, 0]

    for i in range(10):
        if respostas[i] == fishProfiles["TILÁPIA"][i]:
            fishAffinity[0] += 1
        if respostas[i] == fishProfiles["BARBELA"][i]:
            fishAffinity[1] += 1
        if respostas[i] == fishProfiles["SALMONETE"][i]:
            fishAffinity[2] += 1
        if respostas[i] == fishProfiles["PEIXE FOCINHO DE ELEFANTE"][i]:
            fishAffinity[3] += 1
        if respostas[i] == fishProfiles["PETROCEPHALUS BANE"][i]:
            fishAffinity[4] += 1
        if respostas[i] == fishProfiles["BAIACU"][i]:
            fishAffinity[5] += 1

    # print(fishAffinity)

    fishIndex = fishAffinity.index(max(fishAffinity))

    print(
        f"{Fore.CYAN} VOCÊ É UM PEIXE {fishNames[fishIndex]} {Fore.YELLOW}{fishIcon[fishNames[fishIndex]]}{Fore.CYAN} , {fishCharacteristics[fishIndex]}."
    )

    return fishNames[fishIndex]


# tipo_de_peixe = personality_quiz()