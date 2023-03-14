import socket
import sys
import time
import os


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
  command = 'server.exe'


  while True:
    try:
      res = check(host, port)
      if res:
        time.sleep(3)
        continue
    except(TimeoutError):
      os.system(command)
      print('[+] Check the server')
      time.sleep(2)
      continue



if __name__ == '__main__':
  main()