"""lab5 """
import socket
    
"""SERVER"""
def serversideGetPlaySocket():
    """AF_INET family"""
    socketS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    """bind socket to adress"""
    socketS.bind(('127.0.0.1', 60003))
    socketS.listen(1)

    print('\nlistening...\n')
    (socketC, addr) = socketS.accept()
    print('connection from {}'.format(addr))
    socketS.close()    
    print('client {} disconnected'.format(addr))
    return socketC
"""CLIENT"""
def clientsideGetPlaySocket(host):
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 60003))
	
    return sock    		
""" """
def compareMarker(mineMarker, otherMarker):
	if (mineMarker == 'O' and otherMarker == 'X') or \
	(mineMarker == 'X' and otherMarker == 'U') or \
	(mineMarker == 'U' and otherMarker == 'O'):
            return 1
	elif (mineMarker == otherMarker):
	    return 0
	else: 
	    return -1
"""MAIN"""
scoreLs = [0, 0]
maxScore = 2
ans = "?"
while ans not in {"K", "S"}:
    ans = input("Vill du kora som KLIENT eller SERVER (K/S): ")
if ans == "S":
    sock = serversideGetPlaySocket()
else:
    host = input("Ange serverns NAMN eller IP: ")
    sock = clientsideGetPlaySocket(host)

while (scoreLs[0] != maxScore) and (scoreLs[1] != maxScore):
    message = "?"
    while message not in {"O", "U", "X"}:
        message = input('please type your move(O, X, or U): ')
    print("({}, {}) Ditt drag: {}".format(scoreLs[0], scoreLs[1], message))
    mine = message
    sock.sendall(bytearray(mine, 'ascii'))
    other = sock.recv(1024).decode("ASCII")
    print("Motspelarens drag: {}".format(other))
    if compareMarker(mine, other) == 1:
        scoreLs[0] += 1
    elif compareMarker(mine, other) == -1:
        scoreLs[1] += 1
    print('Standings: {}, {}'.format(scoreLs[0], scoreLs[1]))

if scoreLs[0] == maxScore:
    print('You Won')
else:    
    print('You Lost')
sock.close()
