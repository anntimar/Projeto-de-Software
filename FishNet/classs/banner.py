# Banner class

from colorama import Fore
from colorama import Style
from classs.customTerminal import CustomTerminal as ct


class Banner:
    def main():
        ct.clean()
        print(f"{Fore.CYAN}  __  _       _          __        _    ")
        print(f"{Fore.CYAN} / _|(_) ___ | |__    /\ \ \  ___ | |_  ")
        print(f"{Fore.CYAN}| |_ | |/ __||  _ \  /  \/ / / _ \| __| ")
        print(f"{Fore.CYAN}|  _|| |\__ \| | | |/ /\  / |  __/| |_  ")
        print(f"{Fore.CYAN}|_|  |_||___/|_| |_|\_\ \/   \___| \__| ")
        print(f"{Fore.YELLOW}    𓆞       𓆟       𓆛      𓆜      𓆝   ")
        print(f"{Fore.YELLOW}𓆜       𓆜       𓆟      𓆝      𓆛      𓆟")
        print(f"{Style.RESET_ALL}")

    def profile():
        ct.clean()
        print(f"{Fore.CYAN}  __  _       _          __        _   ")
        print(f"{Fore.CYAN} / _|(_) ___ | |__    /\ \ \  ___ | |_ ")
        print(f"{Fore.CYAN}| |_ | |/ __||  _ \  /  \/ / / _ \| __|")
        print(f"{Fore.CYAN}|  _|| |\__ \| | | |/ /\  / |  __/| |_ ")
        print(f"{Fore.CYAN}|_|  |_||___/|_| |_|\_\ \/   \___| \__|")
        print("")
        print(f"{Fore.YELLOW}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{Style.RESET_ALL}")

    def login():
        ct.clean()
        print(f"{Fore.CYAN}   __   ____   _____ ____ _  __")
        print(f"{Fore.CYAN}  / /  / __ \ / ___//  _// |/ /")
        print(f"{Fore.CYAN} / /__/ /_/ // (_ /_/ / /    / ")
        print(f"{Fore.CYAN}/____/\____/ \___//___//_/|_/  ")
        print(f"{Style.RESET_ALL}")

    def create_account():
        ct.clean()
        print(
            f"{Fore.CYAN}  _____ ___   ____ ___    ___    _____ ____   _  __ ______ ___ "
        )
        print(
            f"{Fore.CYAN} / ___// _ \ /  _// _ |  / _ \  / ___// __ \ / |/ //_  __// _ |"
        )
        print(
            f"{Fore.CYAN}/ /__ /   _/_/ / / __ | / , _/ / /__ / /_/ //    /  / /  / __ |"
        )
        print(
            f"{Fore.CYAN}\___//_/|_|/___//_/ |_|/_/|_|  \___/ \____//_/|_/  /_/  /_/ |_|"
        )

        print(f"{Style.RESET_ALL}")

    def personality_quiz():
        ct.clean()
        print(f"{Fore.CYAN}    ____    __  __  ____ _____")
        print(f"{Fore.CYAN}   / __ \  / / / / /  _//__  /")
        print(f"{Fore.CYAN}  / / / / / / / /  / /    / / ")
        print(f"{Fore.CYAN} / /_/ / / /_/ / _/ /    / /_")
        print(f"{Fore.CYAN} \___\_\ \____/ /___/   /____/")

        print(f"{Style.RESET_ALL}")

    def result():
        ct.clean()
        print(
            f"{Fore.CYAN}     ____   ______ _____  __  __ __   ______ ___     ____   ____  "
        )
        print(
            f"{Fore.CYAN}    / __ \ / ____// ___/ / / / // /  /_  __//   |   / __ \ / __ \ "
        )
        print(
            f"{Fore.CYAN}   / /_/ // __/   \__ \ / / / // /    / /  / /| |  / / / // / / / "
        )
        print(
            f"{Fore.CYAN}  / _ _/ / /___  ___/ // /_/ // /___ / /  / ___ | / /_/ // /_/ / "
        )
        print(
            f"{Fore.CYAN} /_/ |_|/_____/ /____/ \____//_____//_/  /_/  |_|/_____/ \____/ "
        )

        print(f"{Style.RESET_ALL}")
