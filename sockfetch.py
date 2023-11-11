import platform
import socket
import psutil
import colorama
from colorama import Fore

colorama.init()

def get_system_info():
    system = platform.system()
    release = platform.release()
    architecture = platform.architecture()[0]
    hostname = socket.gethostname()
    cpu_cores = psutil.cpu_count(logical=False)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert to GB

    return {
        "System": system,
        "Release": release,
        "Architecture": architecture,
        "Hostname": hostname,
        "CPU Cores": cpu_cores,
        "Total Memory": f"{total_memory} GB"
    }

def print_system_info(info):
    for key, value in info.items():
        print(Fore.LIGHTBLUE_EX+ f"{key}: {value}")

    print(""" 
        
              a8888b.
             d888888b.
             8P"YP"Y88
             8|o||o|88
             8'    .88
             8`._.' Y8.
            d/      `8b.
          .dP   .     Y8b.
         d8:'   "   `::88b.
        d8"           `Y88b
       :8P     '       :888
        8a.    :      _a88P
      ._/"Yaa_ :    .| 88P|
 jgs  \    YP"      `| 8P  `.
 a:f  /     \._____.d|    .'
      `--..__)888888P`._.'               
          """)

if __name__ == "__main__":
    system_info = get_system_info()
print_system_info(system_info)
