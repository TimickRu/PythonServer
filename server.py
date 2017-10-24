import socket, classes
from threading import Thread

MAX_CONNS = 5
PORT = 5000

server = socket.socket()
server.bind(('', PORT))
server.listen(MAX_CONNS)
print('Server listening at port ' + str(PORT))
users = []
print('Waiting for connections...')


def stop():
    print('Server stopped.')
    server.close()
    exit()


def cmd():
    while True:
        print('> ', end="")
        cmd = input()
        if cmd == "stop":
            stop()
        else:
            print('Unknown command')


# Запускаем обработчик команд
cmd_thread = Thread(target=cmd, name="cmd")
cmd_thread.start()

while True:
    conn, addr = server.accept()  # Принимаем соединение и записываем его в переменные
    print(addr + " connected!")
    users.append(User(conn, addr, len(users)+1))

