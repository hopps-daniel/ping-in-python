import urllib.request
import socket
import os

hostname = socket.gethostname()

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

ip_address1 = socket.gethostbyname(hostname)

os.system('cls')

#port = [5730, 5731, 5732, 5733, 5734, 5735, 5736, 5737, 5738, 5739]

print("Your external IP is: {} ".format(external_ip))
print("Your internal IP is: {} ".format(ip_address1))
print('-' * 60)

ip_to_check = input('Enter the IP you would like to PING: ')

print('-' * 60)

os.system('ping -n 10 {0}'.format(ip_to_check))

#for number in range(len(port)):
#    print length(port)
#    os.system('ping -n 10 {0}'.format(ip_to_check, port[number]))

print('-' * 60)

input('Press ENTER to exit.')

def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)

kill_by_process_name_shell("cmd.exe")