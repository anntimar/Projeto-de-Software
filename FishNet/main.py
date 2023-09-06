from classs.account import Account
from classs.menu import Menu
from login_screen import login
from create_account_screen import create_account
from app_data import app_data


while True:
    Account("thiago")
    match Menu.main():
        case 1:
            break
        case 2:
            login()
        case 3:
            create_account()
        case 4:
            app_data()

# polimosfismo
