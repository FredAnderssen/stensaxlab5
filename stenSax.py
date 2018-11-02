"""lab5 """
import socket

"""SERVER"""
def serversideGetPlaySocket():
    """AF_INET family"""
    socketS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    """bind socket to adress"""
    socketS.bind(('127.0.0.1', 60003))
    socketS.listen(1)

    while True:
        print('\nlistening...\n')
        (socketC, addr) = socketS.accept()
        print('connection from {}'.format(addr))
        while True:
            data = socketC.recv(1024)
            if not data:
                break
            print('received:', data.decode('ascii'))
            answer = 'thanks for data!'
            socketC.sendall(bytearray(answer, 'ascii'))
            print('answered: ', answer)


        socketC.close()
        print('client {} disconnected'.format(addr))

"""CLIENT"""
def clientsideGetPlaySocket(host):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 60003))

    message = input('please type your message:')
    sock.sendall(bytearray(message, 'ascii'))
    print('sent: ', message)

    data = sock.recv(1024)
    print('recieved: ', data.decode('ascii'))

    sock.close()

"""MAIN"""
ans = "?"
while ans not in {"K", "S"}:
    ans = input("Vill du kora som KLIENT eller SERVER (K/S): ")
if ans == "S":
    sock = serversideGetPlaySocket()
else:
    host = input("Ange serverns NAMN eller IP: ")
    sock = clientsideGetPlaySocket(host)

