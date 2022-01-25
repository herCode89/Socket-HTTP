from socket import *

ServerHost = "gaia.cs.umass.edu"  # Host
ServerPort = 80  # Port
# String to be turned into sequence of byte, ready for transmission
info_requested = b"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

lab = socket(AF_INET, SOCK_STREAM)  # IPv4 address, TCP
lab.connect((ServerHost, ServerPort))  # Web address and Port number passed to connect
lab.send(info_requested)  # Send string to the web server
message = lab.recv(4805)  # Max amount of data to be received
lab.close()  # Close socket
while len(message) > 0:
    print("Request: ", info_requested)  # Print data
    print("Host: ", ServerHost)  # Print the Web address
    print("[RECV] - length: ", len(message))
    print(message.decode())  # UTF-8-encoded string
    break

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
--------------------------------------------------
Author: TRIANGLES
Date: January 01, 2022
URL: https://www.internalpointers.com/post/making-http-requests-sockets-python
Code:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.example.com", 80))
sock.send(b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n")
response = sock.recv(4096)
sock.close()
print(response.decode())

Code 2:
response = b""
while True:
    chunk = sock.recv(4096)
    if len(chunk) == 0:     # No more data received, quitting
        break
    response = response + chunk;

Code 3:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)  # In seconds. Choose a value that makes sense to you
# [...]
response = b""
try:
    while True:
        response = response + sock.recv(4096);
except socket.timeout as e:
    print("Time out!")
'''
