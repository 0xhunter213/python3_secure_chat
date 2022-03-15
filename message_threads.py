from rc4 import enc, dec
import os


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
