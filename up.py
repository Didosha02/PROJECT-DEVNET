import sys
import time
import os
import socket




def check(host, port):

  try:
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    sock.connect((host, port))
    sock.close()

    res = True

    return res
    
  except():
    res = False

    return res

У меня функция check внитри него ip address и номер порта. через переменные проверяем айпи адрес и хост, если в течение 2 секунды не 
прсоединиться то коннекта не будет и не подключиться к серверу и резуьтат будет true и оно возвращает результат в противном случае рузультат будет
false и оно тоже возвращает результат. после создала функцию if __name__ == '__main__':
  main() для проверки был ли файл запущен напрямую. 

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