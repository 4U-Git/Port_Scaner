import socket
from termcolor import colored

host = input(f"\n[+] Introduce la Direccion IP: ")
port = int(input(f"[+] Introduce el Puerto a Escanear: ")) # convertir a entero el puerto

def port_scanner(port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crear socket
    s.settimeout(0.2) # tiempo de espera para la conexion
    
    if s.connect_ex((host, port)): # devuelve un valor, si es 0 esta abierto
        print(f"\n[!] El Puerto {port} Esta cerrado")
    else:
        print(f"\n[+] El Puerto {port} Esta abierto")   
    
    s.close() # cerrar socket
    
def main():
    port_scanner(port) # llamar a la funcion

if __name__ == '__main__':
    main()
