from socket import *

# serverPort = 12000

serverName, serverPort = input('Host/IP Port [Default: localhost 8080]: ' ).split()

if serverPort != '':
    serverPort = int(serverPort)

if serverName == '' and serverPort == '':
    serverName = 'localhost'
    serverPort = 8080

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

    print('Message [{}]: '.format(addr), sentence)

    modifiedMessage = '[{}] OK ::: {}'.format(count, sentence).encode()
    connectionSocket.send(modifiedMessage)

    count += 1

connectionSocket.close()