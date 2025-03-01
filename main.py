

# print("Python code is ran")

# import http.server
# import sys
# import http
# import socketio
# import socketserver
# import socket
# import requests

# print (socket.gethostbyname("192.167.45.23"))


import socket 

html_doc = open("index.html","r")



server_host = "localhost"
server_port = 1313


socket_listen = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket_address = (server_host,server_port)

socket_listen.bind(socket_address)
socket_listen.listen()

connection , address = socket_listen.accept()

print("Got Connection from " , address)

server_msg = connection.recv(1024)
string_request = server_msg.decode()
print(string_request)

string_status = "HTTP/1.1 200 OK"

string_header ="""Content-Type: text/html; charset=UTF-8
    Connection:close

"""

string_content = html_doc

string_response = string_status + string_header + string_content

byte_response = string_response.encode()
connection.send(byte_response)
connection.close()