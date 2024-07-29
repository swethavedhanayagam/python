import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12344
s.bind((host,port))
s.listen(5)
while True:
    C,addr=s.accept()
    print("got connection from",addr)
    s1='''uplink and downlink are separated in time.
    each connection is allotled its own up and downlink pair'''
    C.send(s1.encode())
    C.close()