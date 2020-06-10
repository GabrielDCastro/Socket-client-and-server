import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 25

file = open("shell.txt", 'w')#tudo que ser passado entre o servidor e o cliente será salvo em um arquivo


try:
    server.bind((ip, port)) #bind é pra escutar nessas configurações 
    server.listen(5)        #listen é pra começar de fato a escutar
    print ("Listening in: ", ip, ":", str(port))

    (client_socket, address) = server.accept() #server.accept retorna uma tupla e estamos igualando essa tupla em duas variáveis

    print ("Received from: " + address[0])

    data = client_socket.recv(1024)#especificamos a quantidade de bytes máximos que poderão ser passados
    file.write(data)

    server.close()#fecha a conexão para evitar erros 

except Exception as erro:
    print "Erro: " + str(erro)
    server.close()
