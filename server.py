import socket

HOST = '192.168.3.86'
PORT = 55555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) # Number of connections
print("Listening connections")

# Accept connections
client, address = s.accept()
print("Connected to", address)
# Receive data and decode using utf-8
data = client.recv( 1024 ).decode( 'utf-8' )
print("Received :", repr(data))
client.send("Juanoli".encode("utf-8"))
