import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))  ## Connect to the chat server that we set up earlier by specifying the localhost and port 9999 we defined earlier

done = False



# A basic loop to constantly receive and decode using utf-8. If the message is quit.. the loop is quitted otherwise we print the message and we send a message to server using client.send..
while not done:
    client.send(input("Message: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
            done = True
    else:
        print(msg)