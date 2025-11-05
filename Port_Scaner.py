import socket
from termcolor import colored

host = input(f"\n[+] Introduce la Direccion IP: ")

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crear socket
    s.settimeout(1) # tiempo de espera para la conexion
    return s
    
def port_scanner(port, s):
    
    try:
        s.connect((host, port)) # intentar conectar al puerto
        print(colored(f"[+] Puerto {port} Abierto", 'green')) # puerto abierto
        s.close() # cerrar socket
    
    except (socket.timeout, ConnectionRefusedError):
        s.close() # cerrar socket si no se puede conectar
        
def main():
    
    for port in range(1, 1025): # escanear puertos del 1 al 1024
        s = create_socket() # crear socket
        port_scanner(port, s) # escanear puerto

if __name__ == '__main__':
    main() 
