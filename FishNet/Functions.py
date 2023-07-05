import csv
def sign_up(username,password,email):

    filename = "signup_info.csv"
    data = [[username,password,email]]
    # writing to csv file
    with open(filename, 'a', newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.writer(csvfile)

        # writing data rows
        writer.writerows(data)

def username_list():
    username_list=[]
    with open('signup_info.csv','r') as f:
        for line in f :
            username_list.append(line.split(',')[0])
        return username_list

def extract_matrix(username,password,no):
    password_list = []
    email_list = []
    username_list = []
    with open('signup_info.csv','r') as f:
            for line in f:
                password_list.append(line.split(',')[1])
            for line in f:
                email_list.append(line.split(',')[2])
            for line in f:
                username_list.append(line.split(',')[0])

    data_password = password_list[no]
    while password != data_password:
        print('Incorrect Password')
        user_input = input ("Type R to retry and X to exit: ")
        if user_input == "r" or user_input == "R":
            password = input("Enter Password: ")
        if user_input == "x" or user_input == "X":
            break
    if password == data_password:
       print("Login Successful")
    else:
        print("Invalid Session \n\n")