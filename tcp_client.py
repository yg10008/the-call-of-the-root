import socket
# Imports the socket module, which provides access to network communication.

target_host = "127.0.0.1"  # Example IP address (localhost). Change as needed.
# Sets the target server's IP address. Use a safe, arbitrary IP for public code.

target_port = 12345        # Example port number. Change as needed.
# Sets the target server's port number. Use a safe, arbitrary port for public code.

client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Creates a TCP socket using IPv4 addressing.
# AF_INET for IPv4, SOCK_STREAM for TCP.
# AF_INET6 and SOCK_DGRAM would be used for IPv6 and UDP respectively.

client.connect((target_host,target_port))
# Connects the client socket to the specified host and port.

client.send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n".encode())
# Sends an HTTP GET request to the server. The string is encoded to bytes.

response = client.recv(4096)
# Receives up to 4096 bytes of data from the server.

print(response.decode())
# Decodes the received bytes to a string and prints the server's response.
