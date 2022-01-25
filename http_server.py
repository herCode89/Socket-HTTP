from socket import *
from random import *

HOST = '10.0.0.7'  # Grab Host
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

'''
Author: Python Software Foundation
Date: June 19, 2020
URL: https://docs.python.org/2/library/simplehttpserver.html#module-SimpleHTTPServer
Code: Used for concept to setup
----------------------------------------------
Author: Umangshrestha
Date: July 13, 2021
URL:  https://medium.com/geekculture/implementing-http-from-socket-89d20a1f8f43
Code: 
from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

#############################
# Variables
#############################
HOST, PORT = "127.0.0.1", 8080
response =  b"HTTP/1.1 200 OK\n\nHello World"
#############################

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        try:
            conn, addr = sock.accept()
            req = conn.recv(1024).decode()
            print(req)
            conn.sendall(response)
            conn.close()
        except Exception as E:
            print(E)
Code 2: 
from socket import (
    socket, 
    AF_INET, 
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

#############################
# Variables
#############################
HOST, PORT = "127.0.0.1", 8080
request    = f"GET / HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n".encode()
response   = ""  
#############################

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.connect((HOST, PORT))
    # sending request
    sock.sendall(request)
    # receiving response
    while True:
        recv = sock.recv(1024)
        if recv == b'':
            break
        response += recv.decode()
    print(response)
---------------------------------------------------------------
Author: Emalsha's Blog
URL: https://emalsha.wordpress.com/2016/11/22/how-create-http-server-using-python-socket/
Code: 
import socket   # import socket module 

HOST,PORT = '127.0.0.1',8082 # host -> socket.gethostname() use to set machine IP  

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind((HOST,PORT))
my_socket.listen(1)

Code 2:
while True:
    connection,address = my_socket.accept()
    req = connection.recv(1024).decode('utf-8')

Code 3: 
while True:
   connection,address = my_socket.accept()
   connection.send('Hello world!'.encode('utf-8'))

   connection.close() # close connection
-------------------------------------------------------
Author: Krunal
Date: Aug. 25, 2021
URL: https://appdividend.com/2019/02/06/python-simplehttpserver-tutorial-with-example-http-request-handler/
Code: 
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

Code 2:
python3 -m http.server 8000   (needed the concept to run program)
This site was mostly used to gain an understanding
-------------------------------------------------------------
Author: ThemeZee
Date: July 20, 2015
URL: https://blog.technotesdesk.com/python-exe-no-module-named-simplehttpserver-how-to-run-it-on-windows
Code: 
import SimpleHTTPServer
import SocketServer
PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
-----------------------------------------------------------
'''
