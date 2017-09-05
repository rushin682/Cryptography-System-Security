import socket
import select
import sys
import random
import math

bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = "127.0.0.1"
Port = 9000
bob.connect((IP_address, Port))
 
 
#The MITM values

global p
p=1000
global q
q=3
global y
y=5
#y=random.randint(1,50)
global r2
r2=math.pow(q,y)%p


while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, bob]
 
   
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == bob:
            message = socks.recv(4096)
            message = message.decode()
            print (message)
            print ("The final key for bob is:")
            print (math.pow(float(message),y)%p)
            print("Value being sent is :"+str(r2))
            bob.send(str(r2).encode())   
       
            
        else:
            message=sys.stdin.readline()   
            print("Value being sent is :"+str(r2))
            bob.send(str(r2).encode())
            #sys.stdout.write("<You>")
            #sys.stdout.write(message)
            sys.stdout.flush()
            
bob.close()



