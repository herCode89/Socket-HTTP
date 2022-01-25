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
