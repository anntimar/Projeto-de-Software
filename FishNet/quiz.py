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
        resposta = input(pergunta + " (sim/não): ")

        # Verificando se a resposta é válida
        while resposta.lower() != "sim" and resposta.lower() != "não":
            print("Por favor, responda com 'sim' ou 'não'.")
            resposta = input(pergunta + " (sim/não): ")

        # Armazenando a resposta na lista
        respostas.append(resposta.lower())

    # Avaliando a personalidade baseada nas respostas
    pontuacao = respostas.count("sim")

    print("Resultados do Questionário")
    print("-----------------------------")
    tipo_de_peixe = ""
    if pontuacao >= 9:
        print(
            "Você é um peixe Colisa, muito popular e com facilidade em fazer novos amigos."
        )
        tipo_de_peixe = "Colisa"
    elif pontuacao >= 7:
        print(
            "Você é um peixe Tetra neon, tem uma personalidade popular porém gosta de ser seletivo com suas amizades."
        )
        tipo_de_peixe = "Tetra neon"
    elif pontuacao >= 5:
        print(
            "Você é um peixe Coridora, tem um personalidade amigável e bons hábitos de limpeza!"
        )
        tipo_de_peixe = "Coridora"
    elif pontuacao >= 3:
        print(
            "Você é um peixe Kinguio, tem uma personalidade pacífica e não é bom em fazer amizades."
        )
        tipo_de_peixe = "Kinguio"
    elif pontuacao >= 1:
        print(
            "Você é um peixe Molinésia, tem uma personalidade intensa e bem territorialista."
        )
        tipo_de_peixe = "Molinésia"
    else:
        print(
            "Você é um peixe Arco-íris, tem personalidade forte, sociável que valoriza a rotina."
        )
        tipo_de_peixe = "Arco-íris"

    return tipo_de_peixe
