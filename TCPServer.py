from socket import *                                                                # Módulo/biblioteca para a utilização de sockets

serverData = input('Host/IP Port [Default: localhost 8080]: ')                      # Recebe os dados da conexão

if serverData == '':                                                                # Define padrão para dados da conexão
    serverName = 'localhost'                                                        # Define o nome do servidor (endereço ou IP do servidor)
    serverPort = 8080                                                               # Define a porta do servidor
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)                                         # Cria o socket do servidor, indicando que a rede está usando IPv4 e que o socket será TCP

print('<<< Socket created >>>')

serverSocket.bind(('',serverPort))                                                  # Designa número de porta ao socket do servidor

print('<<< Socket bind complete >>>')

# print('The server is ready to receive')

count = 0

serverSocket.listen(1)                                                              # Escuta requisições de conexão TCP do cliente, indicando número máximo de conexões em fila como 1

while 1:

    connectionSocket, addr = serverSocket.accept()                                  # Cria um novo socket no servidor (connectionSocket) para o cliente que bateu à porta. Cliente e servidor completam apresentação criando uma conexão TCP
    
    sentence = connectionSocket.recv(1024)                                          # Recebe mensagem do cliente. Define tamanho do buffer como 1024

    if sentence.decode() == 'quit':                                                 # Fecha conexão se a mensagem do usuário for "quit"
        connectionSocket.close()
        break

    print('Message [{}]: '.format(addr), sentence.decode())                         # Imprime a mensagem vinda do cliente na tela

    modifiedMessage = '[{}] OK ::: {}'.format(count, sentence.decode()).encode()    # Modifica a mensagem para enviar de volta ao cliente
    connectionSocket.send(modifiedMessage)                                          # Envia mensagem pelo socket específico do cliente para a conexão TCP

    count += 1                                                                      # Incrementa contador de mensagens

    connectionSocket.close()                                                        # Fecha o socket, fechando a conexão TCP entre cliente e servidor

print('<<< Closing connection on server side >>>')