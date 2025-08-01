import socket
# Imports the socket module for network communication.

print("Creating IPv4 UDP socket...")
target_host = "127.0.0.1"  # Example IP address (localhost). Change as needed for public code.
# Sets the target server's IP address. Use a safe, arbitrary IP for public code.

target_port = 12345        # Example port number. Change as needed for public code.
# Sets the target server's port number. Use a safe, arbitrary port for public code.

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Creates a UDP socket using IPv4 addressing.
# AF_INET for IPv4, SOCK_DGRAM for UDP.
# AF_INET6 would be used for IPv6.

print("Socket created.")

print(f"Sending data to {(target_host, target_port)}...")
client.sendto("AAABBBCCC".encode(), (target_host, target_port))
# Sends data to the specified host and port. Data is encoded to bytes.

print("Data sent.")

print("Waiting to receive data...")
data, addr = client.recvfrom(108)
# Receives up to 108 bytes of data from the server.

print("Data received.")

print("Decoded data:", data.decode())
# Decodes the received bytes to a string and prints the data.