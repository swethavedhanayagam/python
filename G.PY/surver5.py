import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''the simple aloha works fine for a light load 
    and does not require any complicated mechanisms.'''
    C.send(s1.encode())
    C.close()