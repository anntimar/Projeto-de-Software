from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def main_banner():
    Fore.CYAN
    print(f"{Fore.CYAN}  __  _       _          __        _    ")
    print(f"{Fore.CYAN} / _|(_) ___ | |__    /\ \ \  ___ | |_  ")
    print(f"{Fore.CYAN}| |_ | |/ __||  _ \  /  \/ / / _ \| __| ")
    print(f"{Fore.CYAN}|  _|| |\__ \| | | |/ /\  / |  __/| |_  ")
    print(f"{Fore.CYAN}|_|  |_||___/|_| |_|\_\ \/   \___| \__| ")
    print(f"{Fore.YELLOW}    𓆞       𓆟       𓆛      𓆜      𓆝   ")
    print(f"{Fore.YELLOW}𓆜       𓆜       𓆟      𓆝      𓆛      𓆟")
    print(f"{Style.RESET_ALL}")



# Slant
def login_banner():
    print(f"{Fore.CYAN}   __   ____   _____ ____ _  __")
    print(f"{Fore.CYAN}  / /  / __ \ / ___//  _// |/ /")
    print(f"{Fore.CYAN} / /__/ /_/ // (_ /_/ / /    / ")
    print(f"{Fore.CYAN}/____/\____/ \___//___//_/|_/  ")
    print(f"{Style.RESET_ALL}")


def create_account_banner():
    print(f"{Fore.CYAN}  _____ ___   ____ ___    ___    _____ ____   _  __ ______ ___ ")
    print(f"{Fore.CYAN} / ___// _ \ /  _// _ |  / _ \  / ___// __ \ / |/ //_  __// _ |")
    print(f"{Fore.CYAN}/ /__ /   _/_/ / / __ | / , _/ / /__ / /_/ //    /  / /  / __ |")
    print(f"{Fore.CYAN}\___//_/|_|/___//_/ |_|/_/|_|  \___/ \____//_/|_/  /_/  /_/ |_|")

    print(f"{Style.RESET_ALL}")
