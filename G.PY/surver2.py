import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12342
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''mac is quite simple,as the only crusial factor 
    is accessing the reserved time slot at the right moment'''
    C.send(s1.encode())
    C.close()