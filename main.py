import urllib.request
import socket
import os

hostname = socket.gethostname()

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

ip_address1 = socket.gethostbyname(hostname)

os.system('cls')

#port = [5730, 5731, 5732, 5733, 5734, 5735, 5736, 5737, 5738, 5739]

print("Tú IP externa es: {} ".format(external_ip))
print("Tú IP interna es: {} ".format(ip_address1))
print('-' * 60)

ip_to_check = input('Ingresa la IP para hacer ping: ')

print('-' * 60)

os.system('ping -n 10 {0}'.format(ip_to_check))

#for number in range(len(port)):
#    print length(port)
#    os.system('ping -n 10 {0}'.format(ip_to_check, port[number]))

print('-' * 60)

print("El mínimo es la mejor conexión posible.")
print("El máximo la peor conexión que se registro.")
print("La media es lo que tendrás normalmente durante la conexión con el otro usuario.")
print('-' * 60)
print("Para juegos online el máximo recomendable como promedio es 150ms, Juega con precaución.")
print('-' * 60)
input('Presiona ENTER para salir.')

def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)

kill_by_process_name_shell("cmd.exe")