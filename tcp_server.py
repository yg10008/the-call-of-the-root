import socket
# Imports the socket module for network communication.

import threading
# Imports threading to handle multiple clients concurrently.

bind_ip = "192.168.56.1"
# The IP address the server will listen on. Change to a safe, arbitrary IP for public code.

bind_port = 8080
# The port number the server will listen on. Change to a safe, arbitrary port for public code.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Creates a TCP socket using IPv4 addressing.
# AF_INET for IPv4, SOCK_STREAM for TCP.
# AF_INET6 and SOCK_DGRAM would be used for IPv6 and UDP respectively.

server.bind((bind_ip, bind_port))
# Binds the server socket to the specified IP address and port.

server.listen(5)
# Starts listening for incoming connections.
# The argument (5) specifies the maximum number of queued connections.

print("[*] Listening on %s:%d" % (bind_ip, bind_port))
# Prints a message indicating the server is listening.

def handle_client(client_socket):
    # Function to handle communication with a connected client.
    request = client_socket.recv(1024)
    # Receives up to 1024 bytes of data from the client.
    print("[*] Received: %s" % request.decode())
    # Prints the received data after decoding from bytes to string.
    client_socket.send(b"ACK")
    # Sends an acknowledgment back to the client.
    client_socket.close()
    # Closes the client socket.

while True:
    # Main server loop to accept incoming connections.
    client, addr = server.accept()
    # Accepts a new connection. Returns the client socket and address.
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    # Prints the address of the connected client.
    client_handler = threading.Thread(target=handle_client, args=(client,))
    # Creates a new thread to handle the client.
    client_handler.start()
    # Starts the client handler thread.