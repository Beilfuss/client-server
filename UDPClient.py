from socket import *

serverData = input('Host/IP Port [Default: localhost 8080]: ')

if serverData == '':
    serverName = 'localhost'
    serverPort = 8080
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)   

clientSocket = socket(AF_INET, SOCK_DGRAM)

while 1:

    message = input("Message to send...: ").encode()
    clientSocket.sendto(message,(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Server reply......: ", modifiedMessage.decode())

clientSocket.close()