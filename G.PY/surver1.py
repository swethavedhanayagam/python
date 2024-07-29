import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12341
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''the simplest algorithm for using tdm is allocating time slots for channels in
    a fixed pattern.this results in a fixed bandwidth
    and is the typical solution for wireless phone systems'''
    C.send(s1.encode())
    C.close()