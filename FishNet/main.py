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
    os.system('cls') or None

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
clean_terminal()
time.sleep(1)
while True:
# ----------------------------------------------------------------
    print(f'{Fore.CYAN}  __  _       _          __        _    {Style.RESET_ALL}')
    print(f'{Fore.CYAN} / _|(_) ___ | |__    /\ \ \  ___ | |_  {Style.RESET_ALL}')
    print(f'{Fore.CYAN}| |_ | |/ __||  _ \  /  \/ / / _ \| __| {Style.RESET_ALL}')
    print(f'{Fore.CYAN}|  _|| |\__ \| | | |/ /\  / |  __/| |_  {Style.RESET_ALL}')
    print(f'{Fore.CYAN}|_|  |_||___/|_| |_|\_\ \/   \___| \__| {Style.RESET_ALL}')
    print(f'{Fore.YELLOW}     𓆞       𓆟       𓆛      𓆜      𓆝   {Style.RESET_ALL}')
    print(f'{Fore.YELLOW} 𓆜       𓆜       𓆟      𓆝      𓆛      𓆟{Style.RESET_ALL}')
    print()

 
    print(f'{Fore.YELLOW} ➀ {Fore.CYAN}LOGIN{Style.RESET_ALL}')
    print(f'{Fore.YELLOW} ➁ {Fore.CYAN}CRIAR CONTA{Style.RESET_ALL}')
    print(f'{Fore.YELLOW} ➂ {Fore.CYAN}SAIR{Style.RESET_ALL}')
    print('')
    action = input(f'{Fore.CYAN} ▷ {Style.RESET_ALL}')
    action = action.upper()  # force lowercase
    action = action[0]  # just use first letter
    clean_terminal()
# ----------------------------------------------------------------

# ----------------------------------------------------------------
    if action == '1':
        print('------ LOGIN ------')

        userEmail= input('E-MAIL: ')
        userEmail = str(userEmail)
        userEmail = userEmail.lower()
        print('')

        userPassword =  pwinput.pwinput('SENHA: ')
        userPassword =  str(userPassword)
        userPassword = userPassword.lower()
        print('')


        if(userEmail in accountDict and accountDict[userEmail]["e-mail"] == userEmail and accountDict[userEmail]['password'] == userPassword):
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
    elif action == '2':
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
    elif action == '3':
        break
# ----------------------------------------------------------------

