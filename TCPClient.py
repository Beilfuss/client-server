from socket import *                                            # Módulo/biblioteca para a utilização de sockets

serverData = input('Host/IP Port [Default: localhost 8080]: ')  # Recebe os dados da conexão

if serverData == '':                                            # Define padrão para dados da conexão
    serverName = 'localhost'                                    # Define o nome do servidor (endereço ou IP do servidor)
    serverPort = 8080                                           # Define a porta do servidor
else:
    serverName, serverPort = serverData.split()
    serverPort = int(serverPort)

while 1:

    clientSocket = socket(AF_INET, SOCK_STREAM)                 # Cria o socket do cliente, indicando que a rede está usando IPv4 e que o socket será TCP
    clientSocket.connect((serverName, serverPort))              # Estabelece conexão com o servidor

    sentence = input('Message to send...: ').encode()           # Recebe mensagem do usuário através do terminal e converte de "str" para "bytes-like"

    if sentence.decode() == 'quit':                             # Fecha conexão se a mensagem do usuário for "quit"
        clientSocket.close()
        break

    clientSocket.send(sentence)                                 # Envia mensagem pelo socket do cliente para a conexão TCP
    
    modifiedSentence = clientSocket.recv(1024)                  # Recebe mensagem do servidor. Define tamanho do buffer como 1024
    print('Server reply......: ', modifiedSentence.decode())    # Imprime a mensagem vinda do servidor na tela

    clientSocket.close()                                        # Fecha o socket, fechando a conexão TCP entre cliente e servidor
