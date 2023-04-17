from socket import *

serverData = input('Host/IP Port [Default: localhost 8080]: ')

if serverData == '':
    serverName = 'localhost'
    serverPort = 8080
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)

while 1:

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    sentence = input('Message to send...: ').encode()
    clientSocket.send(sentence)
    modifiedSentence = clientSocket.recv(1024)
    print('Server reply......: ', modifiedSentence.decode())

clientSocket.close()