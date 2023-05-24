from socket import *
import requests
import json

# URL to the API
url = 'https://plantpalweb.azurewebsites.net/api/sensordatas'

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to server address and server port
serverPort = 7000
serverAddress = ('', serverPort)
serverSocket.bind(serverAddress)

# Print a message to the console to indicate the server is ready.
print("The server is ready")

# Loop forever listening for incoming datagrams
while True:
    message, clientAddress = serverSocket.recvfrom(4096)

    decodedMessage = message.decode()

    # Deserialize the message
    deserializedMessage = json.loads(decodedMessage)

    # Print the message received json data from the client
    print(deserializedMessage)

    # Send a POST request to the API with the message
    r = requests.post(url, json=deserializedMessage)
