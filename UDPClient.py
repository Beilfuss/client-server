from socket import *                                                # Módulo/biblioteca para a utilização de sockets

serverData = input('Host/IP Port [Default: localhost 8080]: ')      # Recebe os dados da conexão

if serverData == '':                                                # Define padrão para dados da conexão
    serverName = 'localhost'                                        # Define o nome do servidor (endereço ou IP do servidor)
    serverPort = 8080                                               # Define a porta do servidor
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)   

clientSocket = socket(AF_INET, SOCK_DGRAM)                          # Cria o socket do cliente, indicando que a rede está usando IPv4 e que o socket será UDP

while 1:

    message = input("Message to send...: ").encode()                # Recebe mensagem do usuário através do terminal e converte de "str" para "bytes-like"
    clientSocket.sendto(message,(serverName, serverPort))           # O método "sendto" acrescenta o endereço de destino (serverName e serverPort) à mensagem e envia o pacote resultante pelo socket do processo (clientSocket)
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    # Recebe mensagem e endereço do servidor. Define tamanho do buffer como 2048
    print("Server reply......: ", modifiedMessage.decode())         # Imprime a mensagem vinda do servidor na tela

clientSocket.close()                                                # Fecha o socket, concluindo o processo