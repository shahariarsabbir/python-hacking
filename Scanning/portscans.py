#! /usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("[+] Enter host to scan: ")
port = int(input("[*] Enter port to scan:  "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(f"Port {port} is closed")
	else:
		print(f"Port {port} is opened")


portscanner(port)

