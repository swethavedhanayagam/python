import socket
import tkinter
from tkinter import*
from tkinter import ttk,font, messagebox 
top=Tk()
top.geometry("400x300")
top.title("guiserverconnect")
l=Label(top,text="port_number").place(relx=0.0,rely=0.1)
e=Entry(top).place(relx=0.1,rely=0.1)
def click():
 s=socket.socket()
 host=socket.gethostname()
 port=12341
 s.connect((host,port))
 a=s.recv(1024)
 print(a.decode()+"i am a client four")
 s.close()
btn=Button(top,text="connect",command=lambda:click()).place(relx=0.1,rely=0.2)
top.mainloop()

