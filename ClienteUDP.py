import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#AF_inet é uma conexão IPV4. SOCK_DGRAM é UDP

try:

    while True:
        client.sendto(input("Voce: ") + "\n", ("127.0.0.1", 666))
        msg, friend = client.recvfrom(1024)
        print friend[0] + ": " + msg

    client.close()
except Exception as erro:
    print ("Conexao falhou")
    print (erro)
    client.close()
