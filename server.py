import socket  ## define the socket module for use 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ## This line creates a new socket and define its a Internet socket (INET) for *Internet Connections* as we want a Internet socket. We define that its a SOCK_STREAM which is a *Stream based* socket meaning its a connection orientated socket using TCP protocol 
server.bind(("localhost", 9999))  #We bind the socket to local host to port 9999


server.listen()  ## listens for incoming client communication


client, addr = server.accept() #Once client request is received we accept the request with the message



done = False


# A basic loop to constantly receive and decode using utf-8. If the message is quit.. the loop is quitted otherwise we print the message and we send a message to client using client.send...
while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else: 
        print(msg)
    client.send(input("Message: ").encode('utf-8'))





## Reference for program: https://youtu.be/Ar94t2XhKzM?si=1p8JKdgSz8YHCdxm