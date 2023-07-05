import time
import os
import pwinput

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


colorama_init()

accountsList = []

accountDict = {}

def newAccount(aName, aPassword,aEmail):
    global accountDict
    newAccountDict = {'name':aName,'password':aPassword,'e-mail': aEmail}
    accountDict[aEmail] = newAccountDict

def clean_terminal():
    print("\n" * os.get_terminal_size().lines)

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
        "Você tem dificuldade em aceitar opiniões contrárias as suas?"
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
    tipo_de_peixe = ''
    if pontuacao >= 9:
        print("Você é um peixe Colisa, muito popular e com facilidade em fazer novos amigos.")
        tipo_de_peixe = 'Colisa'
    elif pontuacao >= 7:
        print("Você é um peixe Tetra neon, tem uma personalidade popular porém gosta de ser seletivo com suas amizades.")
        tipo_de_peixe = 'Tetra neon'
    elif pontuacao >= 5:
        print("Você é um peixe Coridora, tem um personalidade amigável e bons hábitos de limpeza!")
        tipo_de_peixe = 'Coridora'
    elif pontuacao >= 3:
        print("Você é um peixe Kinguio, tem uma personalidade pacífica e não é bom em fazer amizades.")
        tipo_de_peixe = 'Kinguio'
    elif pontuacao >= 1:
        print("Você é um peixe Molinésia, tem uma personalidade intensa e bem territorialista.")
        tipo_de_peixe = 'Molinésia'
    else:
        print("Você é um peixe Arco-íris, tem personalidade forte, sociável que valoriza a rotina.")
        tipo_de_peixe = 'Arco-íris'

    return tipo_de_peixe 

while True:
# ----------------------------------------------------------------
    clean_terminal()
    print('PRESSIONE L PARA INICIAR O LOGIN')
    print('PRESSIONE C PARA OBTER UMA CONTA')
    print('PRESSIONE Q PARA SAIR')
    print()
    action = input('ESCOLHA UMA OPÇÃO:')
    action = action.upper()  # force lowercase
    action = action[0]  # just use first letter
    clean_terminal()
# ----------------------------------------------------------------

# ----------------------------------------------------------------
    if action == 'L':
        print('------ LOGIN ------')

        userEmail= input('E-MAIL: ')
        userEmail = str(userEmail)
        userEmail = userEmail.lower()
        print('')

        userPassword =  pwinput.pwinput('SENHA: ')
        userPassword =  str(userPassword)
        userPassword = userPassword.lower()
        print('')

        # if(accountDict[userEmail]["e-mail"] == userEmail & accountDict[userEmail]['password'] == userPassword):
        aux = accountDict[userEmail]


        if(aux["e-mail"] == userEmail and aux['password'] == userPassword):
            print('')
            print(f'{Fore.GREEN}LOGIN REALIZADO COM SUCESSO!{Style.RESET_ALL}')
            print('')
        else:   
            print('')
            print(f'{Fore.RED}USUARIO OU SENHA INCORRETOS!{Style.RESET_ALL}')
            print('')
        print('')
        questionarioPersonalidade()
        time.sleep(2)
        d = 0
        while d == 0:
            clean_terminal()
            print('PRESSIONE Q PARA SAIR')
            print()
            action = input('ESCOLHA UMA OPÇÃO:')
            action = action.lower()  # force lowercase
            action = action[0]  # just use first letter
            clean_terminal()
            if action == 'q':
                d=1
            clean_terminal()


# ----------------------------------------------------------------

# ----------------------------------------------------------------
    elif action == 'C':
        print('------ CRIE SUA CONTA ------')
        userName= input('ESCOLHA UM NOME DE USUARIO: ')
        userName = str(userName)
        userName = userName.lower()
        print('')

        key1 = '/'
        key2 = '*'
        while key1 != key2:
            userPassword =  pwinput.pwinput('ESCOLHA UMA SENHA: ')
            key1 =  str(userPassword)

            userPassword =  pwinput.pwinput('CONFIRME A SENHA SENHA: ')
            key2 = str(userPassword)

            if(key1 != key2):
                print('')
                print(f'{Fore.RED}SENHA DIFERENTES{Style.RESET_ALL}')
                print('')

        userPassword = str(key2)
        userPassword = userPassword.lower()
        print('')

        userEmail = input('INFORME SEU E-MAIL: ')
        userEmail = str(userEmail)
        userEmail = userEmail.lower()

        newAccount(userName, userPassword, userEmail)

        print('')
        print('CONTA CRIADA COM SUCESSO!')
        print('')
        time.sleep(2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------

