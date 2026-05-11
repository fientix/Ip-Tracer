import os
import requests
import colorama

colorama.init(autoreset=True)

logo = '''
\033[38;2;255;255;255m  ███████╗██╗███████╗███╗   ██╗████████╗██╗██╗  ██╗
\033[38;2;230;230;230m  ██╔════╝██║██╔════╝████╗  ██║╚══██╔══╝██║╚██╗██╔╝
\033[38;2;255;180;180m  █████╗  ██║█████╗  ██╔██╗ ██║   ██║   ██║ ╚███╔╝ 
\033[38;2;255;120;120m  ██╔══╝  ██║██╔══╝  ██║╚██╗██║   ██║   ██║ ██╔██╗ 
\033[38;2;255;60;60m  ██║     ██║███████╗██║ ╚████║   ██║   ██║██╔╝ ██╗
\033[38;2;200;0;0m  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═╝
\033[38;2;150;0;0m  ─────────────────────────────────────────────────
\033[38;2;120;0;0m           [ IP TRACER - BY FIENTIX ]
\033[0m'''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    os.system('title Fientix IP - By Fientix')
    
    print(logo)
    
    x = input('\nBaslamak icin Enter Tusuna Basin (Cikmak icin q): ')
    
    if x.lower() == 'q':
        break
        
    if x == '':
        clear_screen()
        print(logo)
        print("\n" + "\033[38;2;200;0;0m" + "─"*50 + "\033[0m")
        IP = input('\033[1;37mHEDEF IP GIRINIZ: \033[0m')
        
        try:
            r = requests.get(f'http://ip-api.com/json/{IP}')
            data = r.json()
            
            if data.get('status') == 'fail':
                print(f"\n\033[1;31m[!] Hata: {data.get('message', 'Gecersiz IP adresi')}\033[0m")
            else:
                print("\n\033[1;37m[+] Bilgiler Basariyla Getirildi:\033[0m")
                print("\033[38;2;200;0;0m" + "─"*50 + "\033[0m")
                
                fields = {
                    "Country": "country",
                    "Region": "regionName",
                    "City": "city",
                    "Zip": "zip",
                    "ISP": "isp",
                    "IP": "query"
                }
                
                for label, key in fields.items():
                    value = data.get(key, 'N/A')
                    print(f"\033[38;2;255;180;180m{label.ljust(10)}: \033[0m{value}")
                
                print("\033[38;2;200;0;0m" + "─"*50 + "\033[0m")
                
        except Exception as e:
            print(f"\n\033[1;31m[!] Baglanti Hatasi: {e}\033[0m")
            
        input('\n\033[1;37mDevam Etmek icin Enter Tusuna Basiniz...\033[0m')