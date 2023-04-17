from socket import *

serverData = input('Host/IP Port [Default: localhost 8080]: ')

if serverData == '':
    serverName = 'localhost'
    serverPort = 8080
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)

print('<<< Socket created >>>')

serverSocket.bind(('',serverPort))

print('<<< Socket bind complete >>>')

# print('The server is ready to receive')

count = 0

while 1:

    serverSocket.listen(1)

    connectionSocket, addr = serverSocket.accept()
    
    sentence = connectionSocket.recv(1024)

    print('Message [{}]: '.format(addr), sentence.decode())

    modifiedMessage = '[{}] OK ::: {}'.format(count, sentence.decode()).encode()
    connectionSocket.send(modifiedMessage)

    count += 1

connectionSocket.close()