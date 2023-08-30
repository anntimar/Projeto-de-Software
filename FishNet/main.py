from classs.menu import Menu
from login_screen import login
from create_account_screen import create_account

while True:
    match Menu.main():
        case 1:
            break
        case 2:
            login()
        case 3:
            create_account()
