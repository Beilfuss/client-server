from socket import *                                                            # Módulo/biblioteca para a utilização de sockets

serverData = input('Host/IP Port [Default: localhost 8080]: ')                  # Recebe os dados da conexão

if serverData == '':                                                            # Define padrão para dados da conexão
    serverName = 'localhost'                                                    # Define o nome do servidor (endereço ou IP do servidor)
    serverPort = 8080                                                           # Define a porta do servidor
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)   

serverSocket = socket(AF_INET, SOCK_DGRAM)                                      # Cria o socket do servidor, indicando que a rede está usando IPv4 e que o socket será UDP

print('<<< Socket created >>>')

serverSocket.bind(('', serverPort))                                             # Designa número de porta ao socket do servidor

print('<<< Socket bind complete >>>')

# print("The server is ready to receive")

count = 0

while 1:

    message, clientAddress = serverSocket.recvfrom(2048)                        # Recebe mensagem e endereço do cliente. Define tamanho do buffer como 2048

    print('Message [{}]: '.format(clientAddress), message.decode())             # Imprime na tela do servidor a mensagem do cliente

    modifiedMessage = '[{}] OK ::: {}'.format(count, message.decode()).encode() # Modifica a mensagem para enviar de volta ao cliente
    serverSocket.sendto(modifiedMessage, clientAddress)                         # Anexa o endereço do cliente (IP e número de porta) à mensagem

    count += 1                                                                  # Incrementa contador de mensagens

print('<<< Closing connection on server side >>>')