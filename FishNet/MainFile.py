import Functions

start = ""

while start == "" :
    start = input("Type S to Create a Account and Type L to login into your Account:  ")
    Username_List = Functions.username_list()
    if start == "S" or start == "s":
        username = input("Enter a Username: ")
        for user in Username_List:
            while user == username:
                username = input("Username Exists, Try Again: ")
        password = input("Enter a Password: ")
        email_adress = input("Enter Email ID: ")
        Functions.sign_up(username,password,email_adress)
        start = ""

    elif start == "L" or start == "l":
        login_username = input("Enter Your Username: ")
        while login_username not in Username_List:
            print('Username Does not Exist.')
            user_input = input("Type R to retry and X to exit: ")
            if user_input == "r" or user_input == "R":
                login_username = input("Enter Your Username: ")
            if user_input == "x" or user_input == "X":
                break
        if login_username not in Username_List:
            print("Invalid Session \n\n")
            start = ""
        else:
            no = Username_List.index(login_username)
            password = input("Enter a Password: ")
            Functions.extract_matrix(login_username,password,no)
            start = ""

    else:
        print("Invalid Session \n\n")
        start = ""