'''
Copyright (c) 2022 Juan Carlos Bindez
"This project is licensed under the MIT License."
'''


import time
import os

try:
        
    def main():
        header_banner()
        menu_header()

    class Color():
        GREEN = '\033[92m'
        LIGTH_GREEN = '\033[1;92m'
        RED = '\033[91m'
        YELLOW = '\033[93m'
        BLUE = '\033[1;34m'
        MAGENTA = '\033[1;35m'
        BOLD = '\033[;1m'
        CYAN = '\033[1;36m'
        LIGHT_CYAN = '\033[1;96m'
        LIGTH_GREY = '\033[1;37m'
        DARK_GREY = '\033[1;90m'
        BLACK = '\033[1;30m'
        WHITE = '\033[1;97m'
        INVERTE = '\033[;7m'
        RESET = '\033[0m'


    def header_banner():
        print(Color.BLUE +
            '''
                             ____ ____  _   _ 
                 _ __  _   _/ ___/ ___|| | | |
                | '_ \| | | \___ \___ \| |_| |
                | |_) | |_| |___) |__) |  _  |
                | .__/ \__, |____/____/|_| |_|
                |_|    |___/                    v1.0.1

                Copyright (c) 2022 Juan Carlos Bindez

            '''
        + Color.RESET)


    def menu_header():
        print(Color.YELLOW +

            '''
                [Crl + C]  Para Parar o Programa
                
            [1] Mudar Porta SSH
            [2] Start no  Serviço
            [3] Parar Serviço
            [4] Restart Serviço
            [5] Status do Serviço
            '''
        + Color.RESET)

        choice = int(input(">> "))

        if choice == 1:
            port_change()
        
        elif choice == 2:
            start_service()

        elif choice == 3:
            stop_service()

        elif choice == 4:
            restart_service()

        elif choice == 5:
            status_service()

        else:
            print("Digite Apenas os Numeros Listados!")


    def port_change():
        os.system("clear")
        os.chdir('//etc//ssh')
        time.sleep(1)
        os.system("sudo nano sshd_config")
        time.sleep(2)
        port = str(input("Digite a Porta Escolhida \n PORT >> "))
        os.system("sudo iptables -A INPUT -p tcp --dport {} -j ACCEPT".format(port))
        os.system("systemctl restart ssh.service")
        os.system("systemctl status ssh.service")
        main()


    def start_service():
        os.system("clear")
        os.system("systemctl start ssh.service")
        os.system("systemctl status ssh.service")


    def stop_service():
        os.system("clear")
        os.system("systemctl stop ssh.service")
        os.system("systemctl status ssh.service")
        main()


    def restart_service():
        os.system("clear")
        os.system("systemctl restart ssh.service")
        os.system("systemctl status ssh.service")
        main()


    def status_service():
        os.system("clear")
        os.system("systemctl status ssh.service")
        main()


    def scan_port():
        os.system("clear")
        address = str(input("IP >>"))
        os.system("nmap -v {}".format(address))
        main()


    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    os.system("clear")
    header_banner()
