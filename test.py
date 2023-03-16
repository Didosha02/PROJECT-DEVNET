import socket
import sys
import time


def check(host, port):

  try:
    res = False
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    sock.connect((host, port))
    sock.close()

    res = True

    return res
  except():
    res = False

    return res



def main():

  host = sys.argv[1]
  port = 9999
  res = False

  f = open('log.txt', 'w')


  while True:
    try:
      res = check(host, port)
      if res:
        f.write('[+] Server is up!\r\n')
        print('[+] Server is up')
        time.sleep(3)
        continue
    except(TimeoutError):
      f.write('[-] Server is down!\r\n')
      print('[-] Server is down')



if __name__ == '__main__': 
  main()
