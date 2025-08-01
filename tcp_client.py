import socket

target_host = "192.168.56.1"
target_port = 8080

client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

response = client.recv(4096)
print(response.decode())
