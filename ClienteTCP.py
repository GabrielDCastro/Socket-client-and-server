import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_inet é uma conexão IPV4. Sock_stream é TCP
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 889))#clinete vai tentar se conectar nesse ip e na porta 889
    data = input("Mensagem: ")
    client.send(data)

    pacotes_recebidos = client.recv(1024)

    print (pacotes_recebidos)
except:
    print ("Conexao falhou")
