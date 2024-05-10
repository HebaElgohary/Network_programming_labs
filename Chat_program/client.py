from socket import *
s = socket (AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7002

s.connect((host,port))

while True:
    
    y = input("client: ")
    if len(y) > 2048:
       chunk_size = 2048
       for i in range(0, chunk_size):
        s.send((y[i:i+chunk_size]).encode('utf-8'))
    else:
    
       s.send(y.encode('utf-8'))
    if y == "q":
        break

    x= s.recv(2048)
    if x.decode('utf=8') == "q":
        break
    print("server: ", x.decode('utf-8'))
s.close()    