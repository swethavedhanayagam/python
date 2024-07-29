import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12343
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''if this synchronization is assured ,each mobile 
    station know its turn and no interference will happen'''
    C.send(s1.encode())
    C.close()