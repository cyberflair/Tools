import socket
import termcolor

def scan(target, ports)
	print('\n' + 'Starting Scan For' + str(target))
	for port in range (1, ports):
		scan_port (target, port)
def scan_port(ipaddress,port)
	try:
		sock = socket.socket()
		sock.connect((ipaddress,port))
		print("[+] Port Opened" + str(port))
	except: 
		pass
targets = input ("[*] Enter Target To Scan(split them by ,):") #e.g "192.168.1.1, 192.168.1.2"
ports = int(input ("[*] Enter How Many Ports You Want To Scan:"))
scan(targets, ports)
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)

