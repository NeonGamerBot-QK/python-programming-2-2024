from socket import *


server_name = 'localhost'

server_port = 12000


client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((server_name, server_port))


sentence = input('Enter string to be reversed! ')

client_socket.send(sentence.encode())


modified_message = client_socket.recv(2048)


print(modified_message.decode())

client_socket.close()