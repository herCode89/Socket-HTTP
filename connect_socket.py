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
