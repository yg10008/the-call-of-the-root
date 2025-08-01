import socket

print("Creating IPv4 UDP socket...")
target_host = "127.0.0.1"  
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created.")

print(f"Sending data to {(target_host, target_port)}...")
client.sendto("AAABBBCCC".encode(), (target_host, target_port))
print("Data sent.")

print("Waiting to receive data...")
data, addr = client.recvfrom(108)
print("Data received.")

print("Decoded data:", data.decode())