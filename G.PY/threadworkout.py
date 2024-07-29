import threading
import time
import socket
def surver():
    s=socket.socket()
    host=socket.gethostname()
    print(host)
    port=12342
    s.bind((host,port))
    s.listen(5)
    time.sleep(1)
    while True:
        C,addr=s.accept()
        print("got connection from",addr)
        s1='''mac is quite simple,as the only crusial factor 
    is accessing the reserved time slot at the right moment'''
        C.send(s1.encode())
        C.close()
def surver2():
    s=socket.socket()
    host=socket.gethostname()
    print(host)
    port=12343
    s.bind((host,port))
    s.listen(5)
    while True:
        C,addr=s.accept()
        print("got connection from",addr)
        s1=''''if this synchronization is assured ,each mobile 
    station know its turn and no interference will happen'''
        C.send(s1.encode())
        C.close()

def client():
    time.sleep(2)
    s=socket.socket()
    host=socket.gethostname()
    port=12342
    s.connect((host,port))
    a=s.recv(1024)
    print(a.decode()+"I am a client onee")
    time.sleep(1)
    s.close()  
def client2():  
    time.sleep(2)
    s=socket.socket()
    host=socket.gethostname()
    port=12343
    s.connect((host,port))
    a=s.recv(1024)
    print(a.decode()+"I am a client three")
    s.close()
thread1=threading.Thread(target=surver)
thread2=threading.Thread(target=client)
thread1=threading.Thread(target=surver2)
thread2=threading.Thread(target=client2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()