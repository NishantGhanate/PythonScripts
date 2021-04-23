import random 
import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 8080   

# constant's on client & server
primeNumber = 13
GeneratorP =  6

privateKey = 4
publicKey = 9 
             
x = str ( pow(GeneratorP,privateKey) % primeNumber )
print('Generated key at client = {}'.format(x))
s.connect((host, port))
x = x.encode()
s.send(x)
recievedPublicKey = int(s.recv(1024).decode())
print ('Recieved key from server = {}'.format(recievedPublicKey))
decodedKey = pow(recievedPublicKey,privateKey)  % primeNumber
print('Shared secret client side = {}'.format(decodedKey))
s.close()                     


