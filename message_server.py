from concurrent.futures import thread
import socket
import sys
from rc4 import enc, dec
from rsa import *
from Crypto.Util.number import *
import threading
import os
from message_threads import *


def recieve_msg(conn, key):
    while True:
        msgRcv = conn.recv(1024)
        if msgRcv != b'':
            msg = dec(msgRcv.decode(), key)
            print("SENDER:" + msg)
            print(f'THIS is the enc: {msgRcv}')
            if "quit" == msg or "exit" == msg:
                exit(0)


def send_msg(conn, key):
    while True:
        data = input()
        if data != '':
            msg = enc(data, key)
            print(msg)
            conn.sendall(msg.encode())
            print('ME: ', data)
            if "quit" == data or "exit" == data:
                exit(0)


if(len(sys.argv) < 2):
    print('[x] USAGE: message HOST PORT')
    exit(0)

host = sys.argv[1]
port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
conn, addr = server.accept()
print('WELECOME TO secure python3 chat\n=== created by @f2y and @0xhunter213 ===\n')
while conn:
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    e, n = 0, 0
    if(data != b''):
        data = data.decode().split(':')
        if(len(data) == 3 and data[0] == 'INTZ'):
            e, n = int(data[1]), int(data[2])
            print(f'[+] SERVER RECIEVE THE KEYS:\ne={e}\nN={n}')
            key = 'F2y&0xhunter123'
            msg = pow(bytes_to_long(key.encode()), e, n)
            conn.sendall(long_to_bytes(msg))
            print(dec(conn.recv(1024).decode(), key))
            conn.send(enc('lets chat', key).encode())
            print('[X] Connection established')
        t1 = threading.Thread(target=send_msg, args=(conn, key))
        t2 = threading.Thread(target=recieve_msg, args=(conn, key))

        t1.start()
        t2.start()
