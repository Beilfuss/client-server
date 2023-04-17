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

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while 1:

    sentence = input('Message to send...: ').encode()
    clientSocket.send(sentence)
    modifiedSentence = clientSocket.recv(1024)
    print('Server reply......: ', modifiedSentence)

clientSocket.close()