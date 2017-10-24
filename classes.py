from threading import Thread
import socket

class User:
    conn = None
    addr = None
    id = None

    def read_data(self):
        data = conn.recv(1024)
        print('Received data from ' + str(addr) + ': ' + str(data))

    def send_data(self, data):
        conn.send(data)

    def __init__(self, conn, addr, id):
        self.conn = conn
        self.addr = addr
        self.id = id
        rxthread = Thread(target=read_data, name="read_data")
        rxthread.start()

