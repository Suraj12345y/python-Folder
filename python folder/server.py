import socket
from textblob import TextBlob

s=socket.socket()
host=socket.gethostname()
print('Server will start at host : '.host)
port=8080
s.blind((host,port))
print("waiting for connection \n")
s.listen(1)
conn,addr=s.accept()
while 1:
    message=input(str('you >>'))
    message=message.encode()
    conn.send(message)
    print("sent \n")
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    blob=TextBlob(incoming_message)
    incoming_message=blob.translate(to='en')
    print('friend >>',incoming_message, '\n')