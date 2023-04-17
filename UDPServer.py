from socket import *

# serverPort = 12000

serverName, serverPort = input('Host/IP Port [Default: localhost 8080]: ' ).split()

if serverPort != '':
    serverPort = int(serverPort)

if serverName == '' and serverPort == '':
    serverName = 'localhost'
    serverPort = 8080

serverSocket = socket(AF_INET, SOCK_DGRAM)

print('<<< Socket created >>>')

serverSocket.bind(('', serverPort))

print('<<< Socket bind complete >>>')

# print("The server is ready to receive")

count = 0

while 1:

    message, clientAddress = serverSocket.recvfrom(2048)

    print('Message [{}]: '.format(clientAddress), message)

    modifiedMessage = '[{}] OK ::: {}'.format(count, message).encode()
    serverSocket.sendto(modifiedMessage, clientAddress)

    count += 1