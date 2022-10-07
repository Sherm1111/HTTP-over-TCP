from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 4444))
server_socket.listen(1)

print("Server is ready to receive...\n")

while(True):
    connection_socket, address = server_socket.accept()
    #print("Connection established.\n")
    
    try:
        #server_host = connection_socket.recv(2048).decode()
        incoming_message = (connection_socket.recv(2048)).decode()
        #print("Received Message: {}".format(incoming_message.decode())) #the '.decode' turns the bytes into a string
        
        #modified_message = incoming_message.upper()
        #print("Modified message: {}".format(modified_message.decode()))
        
        print("HTTP request: {}".format(incoming_message))
        print("Host: {}\n".format(address[0]))
        
        with open("{}".format(incoming_message)) as f:
            msg = "".join(f.readlines())
        
        # file_name = incoming_message.split()[1]
        
        # f = open(file_name[1:])
        
        # data = f.read()
        
        print("Object to be fetched: {}".format(incoming_message))
        print("Object content: \n{}\n".format(msg))
        
        resp_message = "HTTP/1.1 200 OK\n" + msg

        connection_socket.send(msg.encode())

        #print("\nHTTP response message: \n{}\n".format(resp_message))
        connection_socket.close()
        
    except:
        #print("Object to be fetched: {}".format("index.html"))
        resp_message = "HTTP response message: \nHTTP/1.1 404 Not Found"
        #print("\nHTTP response message: \n{}\n".format(resp_message))
        
        connection_socket.send(resp_message.encode())
        
        connection_socket.close()
