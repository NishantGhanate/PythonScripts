import random 
import socket               

s = socket.socket()         
print(s)
host = socket.gethostname() 
print(host)
port = 8080                

# constant's
primeNumber = 13
GeneratorP =  6

privateKey = 5 
publicKey = 2
x = str ( pow(GeneratorP,privateKey) % primeNumber )
print('Generated key at server = {}'.format(x))
s.bind((host, port))        
s.listen(5)           
c, addr = s.accept()     
print ('Got connection from', addr)
recievedPublicKey = int(c.recv(1024).decode())
print ('Recieved key from client = {}'.format(recievedPublicKey))
c.send(x.encode())
# # sender server key 
decodedKey = pow(recievedPublicKey,privateKey)  % primeNumber
print('Shared secret client side = {}'.format(decodedKey))
c.close()               
