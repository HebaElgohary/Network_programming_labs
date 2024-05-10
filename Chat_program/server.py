from socket import *
s = socket (AF_INET, SOCK_STREAM)
print("socket successfully created")

host = "127.0.0.1"
port = 7002

s.bind((host,port))
print("socket binded to ", port)
 
s.listen(5)
print("socket is listening...")

c, addr = s.accept()
print("Get Connection from", addr[0])
full_message = ""
while True:
    chunk =( c.recv(2048).decode('utf-8'))  # Receive data in chunks of 1024 bytes
    if not chunk:
            break  # No more data to receive, break out of the loop
    #full_message += chunk
   # message = full_message#.decode('utf-8')
    print("client: "+chunk)
    y = input("server: ")
    if len(y) > 2048:
       chunk_size = 2048
       for i in range(0, chunk_size):
        c.send((y[i:i+chunk_size]).encode('utf-8'))
    else:
    
       c.send(y.encode('utf-8'))
    if y == "q":
        break

   
c.close() # session must be closed
    