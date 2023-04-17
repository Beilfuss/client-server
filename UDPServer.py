from socket import *

serverData = input('Host/IP Port [Default: localhost 8080]: ')

if serverData == '':
    serverName = 'localhost'
    serverPort = 8080
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)   

serverSocket = socket(AF_INET, SOCK_DGRAM)

print('<<< Socket created >>>')

serverSocket.bind(('', serverPort))

print('<<< Socket bind complete >>>')

# print("The server is ready to receive")

count = 0

while 1:

    message, clientAddress = serverSocket.recvfrom(2048)

    print('Message [{}]: '.format(clientAddress), message.decode())

    modifiedMessage = '[{}] OK ::: {}'.format(count, message.decode()).encode()
    serverSocket.sendto(modifiedMessage, clientAddress)

    count += 1