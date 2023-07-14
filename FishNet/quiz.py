from colorama import init as colorama_init
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
        "tilápia": "𓆛",
        "barbela": "𓆜",
        "salmonete": "𓆝",
        "peixe focinho de elefante": "𓆞",
        "Petrocephalus bane": "𓆟",
        "baiacu": "𓆡",
    }
    fishCharacteristics = [
        "MUITO POPULAR E COM FACILIDADE EM FAZER NOVOS AMIGOS",
        "TEM UMA PERSONALIDADE POPULAR PORÉM GOSTA DE SER SELETIVO COM SUAS AMIZADES",
        "TEM UM PERSONALIDADE AMIGÁVEL E BONS HÁBITOS DE LIMPEZA",
        "TEM UMA PERSONALIDADE PACÍFICA E NÃO É BOM EM FAZER AMIZADES",
        "TEM UMA PERSONALIDADE INTENSA E BEM TERRITORIALISTA",
        "",
    ]

    fishProfiles = {
        "tilápia": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "barbela": [2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        "salmonete": [2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
        "peixe focinho de elefante": [2, 2, 2, 2, 2, 1, 1, 1, 1, 1],
        "Petrocephalus bane": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        "baiacu": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    }

    fishNames = [
        "tilápia",
        "barbela",
        "salmonete",
        "peixe focinho de elefante",
        "Petrocephalus bane",
        "baiacu",
    ]

    fishAffinity = [0, 0, 0, 0, 0, 0]

    for i in range(10):
        if respostas[i] == fishProfiles["tilápia"][i]:
            fishAffinity[0] += 1
        if respostas[i] == fishProfiles["barbela"][i]:
            fishAffinity[1] += 1
        if respostas[i] == fishProfiles["salmonete"][i]:
            fishAffinity[2] += 1
        if respostas[i] == fishProfiles["peixe focinho de elefante"][i]:
            fishAffinity[3] += 1
        if respostas[i] == fishProfiles["Petrocephalus bane"][i]:
            fishAffinity[4] += 1
        if respostas[i] == fishProfiles["baiacu"][i]:
            fishAffinity[5] += 1

    # print(fishAffinity)

    fishIndex = fishAffinity.index(max(fishAffinity))

    print(
        f"{Fore.CYAN} VOCÊ É UM PEIXE {fishNames[fishIndex]} {Fore.YELLOW}{fishIcon[fishNames[fishIndex]]}{Fore.CYAN} ,{fishCharacteristics[fishIndex]}."
    )

    return fishNames[fishIndex]


# tipo_de_peixe = personality_quiz()
