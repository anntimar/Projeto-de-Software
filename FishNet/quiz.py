def questionarioPersonalidade():
    print("Questionário de Personalidade")
    print("-----------------------------")

    # Definindo as perguntas
    perguntas = [
        "Você gosta de se aventurar em novas atividades?",
        "Você se considera uma pessoa extrovertida?",
        "Você se preocupa muito com o que os outros pensam de você?",
        "Você tende a planejar suas atividades com antecedência?",
        "Você se sente confortável em situações sociais?",
        "Você é uma pessoa organizada?",
        "Você gosta de assumir riscos?",
        "Você costuma se estressar facilmente?",
        "Você se considera uma pessoa criativa?",
        "Você tem dificuldade em aceitar opiniões contrárias as suas?",
    ]

    # Criando uma lista para armazenar as respostas
    respostas = []

    # Loop para fazer as perguntas
    for pergunta in perguntas:

        resposta = input((f"{Fore.CYAN} {pergunta} {Fore.YELLOW} ➀{Fore.CYAN} SIM /{Fore.YELLOW} ➁ {Fore.CYAN}NÃO: {Fore.CYAN} ➤  {Fore.YELLOW}"))

        # Verificando se a resposta é válida
        while resposta.lower() != "1" and resposta.lower() != "2":
            print(f"{Fore.RED} ✖ POR FAVOR, RESPONDA COM '1 PARA SIM' OU '2 PARA NÃO'. {Style.RESET_ALL}")
            time.sleep(1)
            resposta = input((f"{Fore.CYAN} {pergunta} {Fore.YELLOW} ➀{Fore.CYAN} SIM /{Fore.YELLOW} ➁ {Fore.CYAN} NÃO: {Fore.CYAN} ➤  {Fore.YELLOW}"))

        # Armazenando a resposta na lista
        respostas.append(resposta.lower())

    # Avaliando a personalidade baseada nas respostas
    pontuacao = respostas.count("1")

    clean_terminal()

    result_banner()

    print("Resultados do Questionário")
    print("-----------------------------")
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
            f"{Fore.CYAN} VOCÊ É UM PEIXE CORIDORA, TEM UMA PERSONALIDADE AMIGÁVEL E BONS HÁBITOS DE LIMPEZA."
        )
        tipo_de_peixe = "Coridora"
    elif pontuacao >= 3:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE KINGUIO, TEM UMA PERSONALIDADE ACÍFICA E NÃO É BOM EM FAZER AMIZADES" 
        )
        tipo_de_peixe = "Kinguio"
    elif pontuacao >= 1:
        print(
            f"{Fore.CYAN} VOCÊ É UM PEIXE MOLINÉSIA, TEM UMA PERSONALIDADE INTENSA E É BEM TERRITORIALISTA."
        )
        tipo_de_peixe = "Molinésia"
    else:
        print(
           f"{Fore.CYAN} VOCÊ É UM PEIXE ARCO-ÍRIS, TEM UMA PERSONALIDADE CALMA E É BOM EM FAZER AMIZADES."
        )
        tipo_de_peixe = "Arco-íris"

    return tipo_de_peixe

    # retomar à funcao
    
    personality_quiz()
