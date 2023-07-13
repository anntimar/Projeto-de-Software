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
        resposta = input(
            (
                f"{Fore.CYAN} {pergunta} {Fore.YELLOW} ➀{Fore.CYAN} SIM /{Fore.YELLOW} ➁ {Fore.CYAN}NÃO: {Fore.CYAN} ➤  {Fore.YELLOW}"
            )
        )

        # Verificando se a resposta é válida
        while resposta.lower() != "1" and resposta.lower() != "2":
            print(
                f"{Fore.RED} ✖ POR FAVOR, RESPONDA COM '1 PARA SIM' OU '2 PARA NÃO'. {Style.RESET_ALL}"
            )
            time.sleep(1)
            resposta = input(
                (
                    f"{Fore.CYAN} {pergunta} {Fore.YELLOW} ➀{Fore.CYAN} SIM / {Fore.YELLOW}➁{Fore.CYAN} NÃO: {Fore.CYAN} ➤   {Fore.YELLOW}"
                )
            )

        # Armazenando a resposta na lista
        respostas.append(resposta.lower())

    # Avaliando a personalidade baseada nas respostas
    pontuacao = respostas.count("1")

    clean_terminal()

    result_banner()

    tipo_de_peixe = ""
    if pontuacao >= 9:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE COLISA, MUITO POPULAR E COM FACILIDADE EM FAZER NOVOS AMIGOS."
        )
        tipo_de_peixe = "Colisa"
    elif pontuacao >= 7:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE TETRA NEON, TEM UMA PERSONALIDADE POPULAR PORÉM GOSTA DE SER SELETIVO COM SUAS AMIZADES."
        )
        tipo_de_peixe = "Tetra neon"
    elif pontuacao >= 5:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE CORIDORA, TEM UM PERSONALIDADE AMIGÁVEL E BONS HÁBITOS DE LIMPEZA!"
        )
        tipo_de_peixe = "Coridora"
    elif pontuacao >= 3:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE KINGUIO, TEM UMA PERSONALIDADE PACÍFICA E NÃO É BOM EM FAZER AMIZADES."
        )
        tipo_de_peixe = "Kinguio"
    elif pontuacao >= 1:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE MOLINÉSIA, TEM UMA PERSONALIDADE INTENSA E BEM TERRITORIALISTA."
        )
        tipo_de_peixe = "Molinésia"
    else:
        print(f"{Fore.CYAN} ")
        tipo_de_peixe = "Arco-íris"

    return tipo_de_peixe

    # retomar à funcao

    personality_quiz()
