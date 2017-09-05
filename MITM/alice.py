import socket
import select
import sys
import random
import math
 
alice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = "127.0.0.1"
Port = 9000
alice.connect((IP_address, Port))


#MITM Values
global p
p=1000
global q
q=3
global x
x=6
#x=random.randint(1,50)
global r1
r1=math.pow(q,x)%p


while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, alice]
 

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == alice:

            message = socks.recv(4096)
            message = message.decode()
            print (message)
            print ("The final key for alice is:")
            print (math.pow(float(message),x)%p)   
            print("Value being sent is :"+str(r1))
            alice.send(str(r1).encode())   


        else:
            message=sys.stdin.readline()  
            print("Value being sent is :"+str(r1))         
            alice.send(str(r1).encode())
            #sys.stdout.write("<You>")
            #sys.stdout.write(message)
            sys.stdout.flush()
alice.close()



