import socket
s=socket.socket()
host=socket.gethostname()
while(s):
    port=12342
s.connect((host,port))
a=s.recv(1024)
print(a.decode()+"I am a client two")
s.close()