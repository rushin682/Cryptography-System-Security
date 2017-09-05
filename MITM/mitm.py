import socket
import select
import sys
import _thread
import random 
import math

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 

 
IP_address = "127.0.0.1"
 
Port = 9000
 

server.bind((IP_address, Port))
 

server.listen(2)

#The MITM values

global p
p=1000
global q
q=3
global z
z=10
global rm
rm=math.pow(q,z)%p

list_of_clients = []


 
def clientthread(conn, addr):
 
    #conn.send("Welcome to this chatroom!".encode())
    #while True:
            try:
                message = conn.recv(4096)
                message=message.decode()
                if message:                    
                    print (message)
                    print ("The final key for this client is:")
                    xyz=math.pow(float(message),z)%p
                    print (xyz)
                    #message_to_send=message
                    #broadcast(message_to_send, conn)
                    broadcast(conn)
                else:
                   
                    remove(conn)
 
            except:
                pass
 

#def broadcast(message, connection):
def broadcast(connection):
    for clients in list_of_clients:
        if clients!=connection:
          try:         
              clients.send(str(rm).encode())
          except:
              clients.close()
 
              remove(clients)
 

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
 
while True:
 
    print("here")
    conn, addr = server.accept()
    print("here now")
    list_of_clients.append(conn)
 
    print (addr[0] + " connected")
 
 
    _thread.start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()
