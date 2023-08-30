import time
from fish_data import *
from classs.banner import Banner
from classs.customTerminal import CustomTerminal as ct

from colorama import Fore
from colorama import Style


def personality_quiz():
    Banner.personality_quiz()

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

    ct.clean()

    fishAffinity = [0, 0, 0, 0, 0, 0]

    for i in range(10):
        if respostas[i] == fishProfiles[0][i]:
            fishAffinity[0] += 1
        if respostas[i] == fishProfiles[1][i]:
            fishAffinity[1] += 1
        if respostas[i] == fishProfiles[2][i]:
            fishAffinity[2] += 1
        if respostas[i] == fishProfiles[3][i]:
            fishAffinity[3] += 1
        if respostas[i] == fishProfiles[4][i]:
            fishAffinity[4] += 1
        if respostas[i] == fishProfiles[5][i]:
            fishAffinity[5] += 1

    # print(fishAffinity)

    fishIndex = fishAffinity.index(max(fishAffinity))

    print(
        f"{Fore.CYAN} VOCÊ É UM PEIXE {fishNames[fishIndex]} {Fore.YELLOW}{fishIcon[fishIndex]}{Fore.CYAN} , {fishCharacteristics[fishIndex]}."
    )
    time.sleep(3)
    return fishIndex
