from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

server_ip = input("Server IP: ")
server_port = input("Port: ")
HTTP_connection = input("Message: ")

client_socket.connect((server_ip, int(server_port)))
client_socket.send(HTTP_connection.encode())
#client_socket.send(message.encode())

request = ("GET \{} HTTP/1.1".format(HTTP_connection))
print("\nHTTP request to server: {}".format(request))
print("Host: {}".format(server_ip))

client_socket.send(request.encode())

received_message = client_socket.recv(2048)
print("\nHTTP response from server: \n{}".format(received_message.decode()))

#file_content = client_socket.recv(2048)

#print("\n{}".format(file_content.decode()))

client_socket.close()
