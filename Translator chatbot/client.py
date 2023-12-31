import socket
from textblob import TextBlob

s=socket.socket()
host=input(str('Enter the Host name to connect : '))
port=8080
print('connected to chat server')
while 1:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    blob=TextBlob(incoming_message)
    incoming_message=blob.translate(to='es')
    print('friend >>',incoming_message,'\n')
    message=input(str('you >>'))
    message=message.encode()
    s.send(message)
    print("sent \n")