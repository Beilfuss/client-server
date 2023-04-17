from socket import *

'''
serverName = 'ine5615.matheus.beilfuss.vms.ufsc.br'
serverPort = 12000
'''

serverName, serverPort = input('Host/IP Port [Default: localhost 8080]:' ).split()

if serverPort != '':
    serverPort = int(serverPort)

if serverName == '' and serverPort == '':
    serverName = 'localhost'
    serverPort = 8080

clientSocket = socket(AF_INET, SOCK_DGRAM)

while 1:

    message = input("Message to send...: ").encode()
    clientSocket.sendto(message,(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Server reply......: ", modifiedMessage)

clientSocket.close()