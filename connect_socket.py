from socket import *

ServerHost = "gaia.cs.umass.edu"  # Server
ServerPort = 80  # Host
# Data to be sent
info_requested = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
client = socket(AF_INET, SOCK_STREAM)  # IPv4 and TCP
client.connect((ServerHost, ServerPort))  # Connect Host and Port
client.send(info_requested.encode())
message = client.recv(1024)  # received the data
client.close()  # close socket
# Display response
print("Request: ", info_requested)
print("[RECV] - length: ", len(message))
print(message.decode())

'''
Authors: James F. Kurose and Keith W. Ross
Title: Computer Networking 
       A Top-Down Approach 8th edition
Code (pg 186):
from socket import *
serverName = 'localhost'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input Lowercase Sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

Code 2 (pg 191):
from socket import *
serverName = 'localhost'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input Lowercase Sentence: ')
clientSocket.send(sentence.encode())
modifiedMessage = clientSocket.recv(1024)
print('From Server: ', modifiedMessage.decode())
clientSocket.close()

-----------------------------------------------------------------
Author: Nathan Jennings
URL: https://realpython.com/python-sockets/#socket-api-overview
Code:
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
Code 2:
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))

Code 3:
if recv_data:
    data.outb += recv_data
else:
    print('closing connection to', data.addr)
    sel.unregister(sock)
    sock.close()
---------------------------------------------------
Author:  Python Software Foundation
URL: https://docs.python.org/3/library/socket.html
Code: 
HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))

Code 2: Overview of looking through the site information
--------------------------------------------------------------
Author: Coulid (JEGX)
Date: December 20, 2021
URL: https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
Code:
target_host = "www.google.com" 

target_port = 80  # create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# connect the client 
client.connect((target_host,target_port))  

# send some data 
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
client.send(request.encode())  

# receive some data 
response = client.recv(4096)  
http_response = repr(response)
http_response_len = len(http_response)

#display the response
gh_imgui.text("[RECV] - length: %d" % http_response_len)
gh_imgui.text_wrapped(http_response)
'''
