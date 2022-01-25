from socket import *
from random import *

HOST = 'localhost'  # Grab Host
PORT = 8002  # Set Port
# IPv4 and TCP
server = socket(AF_INET, SOCK_STREAM)
# server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #was not needed
server.bind((HOST, PORT))  # Bind host and port for communication
server.listen(1)  # socket to listen
print("Connected by: ", (HOST, PORT))  # Print Connected host and port
while True:  # Socket to accept request in a loop
    connect, address = server.accept()  # Return a client socket
    message = connect.recv(1024).decode()
    data = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"
            "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n")
    connect.sendall(data.encode())
    print("Received: ", message)  # Print received message
    print("Sending>>>>>>>> \n\n", data, "<<<<<<<< \n\n")  # Print sent data
    connect.close()  # Close connection
    server.close()  # close server connection
