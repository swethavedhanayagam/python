from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk, Image
# import pymysql as mysql
# from telnetlib import SB
import turtle
# from tkinter import *
# from tkinter import font,messagebox,ttk
# from PIL import ImageTk,Image
import os
win=turtle.Screen()
s=turtle.Turtle()


def circle(s):
    #circle
    s.setposition(0,-280)
    s.pendown()
    s.begin_fill()
    s.color("purple")
    s.pencolor("white")
    s.circle(300)
    s.end_fill()
    s.penup()
def circle2(s):
    #circle2
    s.pensize(2)
    s.setposition(0,-230)
    s.pendown()
    s.begin_fill()
    s.color("skyblue")
    s.pencolor("black")
    s.circle(250)
    s.end_fill()
    s.penup()
def circles(s):
    s.penup()
    s.setpos(-70,50)
    s.pendown()
    s.begin_fill()
    s.color("red")
    s.left(10)
    s.pendown()
    s.pensize(10)
    s.pencolor("white")
    s.speed(1)
    s.right(70)
    s.forward(100)
    s.left(140)
    s.forward(100)
    s.right(150)
    s.forward(100)
    s.left(140)
    s.forward(100)
    s.right(40)
    s.forward(50)
    s.left(40)
    s.backward(150)
    s.left(122)
    s.forward(30)
    s.left(115)
    s.backward(25)
    s.right(70)
    s.forward(30)
    s.right(35)
    s.forward(30)
    s.right(75)
    s.forward(180)
    s.left(40)
    s.backward(70)
    s.end_fill()
    # s.left(40)
    # s.forward(80)
    # s.right(30)
    # s.backward(90)
    # s.left(45)
    # s.forward(230)
    # s.left(30)
    # s.backward(65)
    # s.end_fill()

  
win = turtle.Screen()
win.bgcolor('black')

logo = turtle.Turtle()
logo.speed(10)
logo.pensize(10)
logo.penup()

circle(logo)
circle2(logo)
circles(logo)
# logo.penup()

# logo.setposition(300,300)
# logo.pencolor("red")

# logo.write("Code by swetha")
# logo.hideturtle()
# turtle.done()
s.end_fill()
win.bye()



def customerloginpage(data,win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f1=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.5,rely=0.00)
    f1.pack()
    frame1=Frame(win,width=400,height=470,bg="pink")
    frame1.place(relx=0.35,rely=0.25)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="CustomerLogin Page",bg="green",fg="white",font=label_font)
    b.place(relx=0.41,rely=0.16)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name  "+data[0],font=label_font)
    l1.place(relx=0.37,rely=0.31)
    l2=Label(win,text="Aadhar No  "+data[1],font=label_font)
    l2.place(relx=0.37,rely=0.41)
    l3=Label(win,text="Pan No  "+data[2],font=label_font)
    l3.place(relx=0.37,rely=0.51)
    l4=Label(win,text="Contact  "+data[3],font=label_font)
    l4.place(relx=0.37,rely=0.61)
    l5=Label(win,text="Email ID  "+data[4],font=label_font)
    l5.place(relx=0.37,rely=0.71)
    l6=Label(win,text="Address  "+data[5],font=label_font)
    l6.place(relx=0.37,rely=0.81)
    print(data)

    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f2=Label(win,text="@swetha",font=label_font,bg="blue",fg="white")
    f2.place(relx=0.50,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Customer Registration",bg="green",fg="white",font=label_font,command=lambda:custreg(win))
    b.place(relx=0.04,rely=0.1)
    b1=Button(win,text="Admin Login",bg="green",fg="white",font=label_font,command=lambda:adminlog(win))
    b1.place(relx=0.04,rely=0.2)
    b2=Button(win,text="Customer Login",bg="green",fg="white",font=label_font,command=lambda:customerlog(win))
    b2.place(relx=0.04,rely=0.3)
    b3=Button(win,text="Exit",bg="green",fg="white",font=label_font,command=lambda:exit(win))
    b3.place(relx=0.04,rely=0.6)
    win.mainloop()
      
def customerlog(win):
    win.destroy()
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    frame1=Frame(win,width=400,height=250,bg="pink")
    frame1.place(relx=0.35,rely=0.35)
    
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f1=Label(win,text="ICICI BANK",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.5,rely=0.00)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Customer Login",bg="green",fg="white",font=label_font)
    b.place(relx=0.43,rely=0.23)

    label_font=font.Font(win,weight="bold",family="Times New Roman",size=20)
    l=Label(win,text="Customer ID",font=label_font).place(relx=0.37,rely=0.41)
    l=Label(win,text="Password",font=label_font).place(relx=0.37,rely=0.51)
    e1=Entry(win)
    e1.place(relx=0.49,rely=0.41,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.49,rely=0.51,width=150,height=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b1=Button(win,text="Login",bg="green",font=label_font,command=lambda:customerlogin1(e1.get(),e2.get(),win))
    b1.place(relx=0.49,rely=0.60) 
    f1=Frame(win,width=350,height=750,bg="pink")
    f1.place(relx=0.00,rely=0.06)
    frame=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f2=Label(win,text="@swetha",font=label_font,bg="blue",fg="white")
    f2.place(relx=0.50,rely=0.94)
    frame.place(relx=0.00,rely=0.94)
    b3=Button(win,text="Customer Registration",bg="green",fg="white",font=label_font,command=lambda:custreg(win))
    b3.place(relx=0.04,rely=0.1)
    b4=Button(win,text="Admin Login",bg="green",fg="white",font=label_font,command=lambda:adminlog(win))
    b4.place(relx=0.04,rely=0.2)
    b5=Button(win,text="Customer Login",bg="green",fg="white",font=label_font,command=lambda:customerlog(win))
    b5.place(relx=0.04,rely=0.3)
    b6=Button(win,text="Exit",bg="green",fg="white",font=label_font,command=lambda:exit(win))
    b6.place(relx=0.04,rely=0.6) 
    def  customerlogin1(a,b,win):
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
        cursor=connection.cursor()
        result="select * from student where Name='"+e1.get()+"'and Contact='"+e2.get()+"'"
        cursor.execute(result)
        print(result)
        r=0
        for x in cursor:
            customerloginpage(x,win)
            r=r+1
        if r>0:
            print("loggin")
        else:
            print("not loggin")
    win.mainloop()      

def custreg(win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    frame1=Frame(win,width=400,height=530,bg="pink")
    frame1.place(relx=0.35,rely=0.20)
    f=Frame(win,width=1500,height=500,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.5,rely=0.00)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Customer Registration",bg="green",fg="white",font=label_font)
    b.place(relx=0.40,rely=0.14)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name",font=label_font).place(relx=0.38,rely=0.23)
    l2=Label(win,text="Aadhar No",font=label_font).place(relx=0.38,rely=0.33)
    l3=Label(win,text="Pan No",font=label_font).place(relx=0.38,rely=0.43)
    l4=Label(win,text="Contact",font=label_font).place(relx=0.38,rely=0.53)
    l5=Label(win,text="Email ID",font=label_font).place(relx=0.38,rely=0.63)
    l6=Label(win,text="Address",font=label_font).place(relx=0.38,rely=0.73)
    e1=Entry(win)
    e1.place(relx=0.50,rely=0.24,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.50,rely=0.34,width=150,height=30)
    e3=Entry(win)
    e3.place(relx=0.50,rely=0.44,width=150,height=30)
    e4=Entry(win)
    e4.place(relx=0.50,rely=0.54,width=150,height=30)
    e5=Entry(win)
    e5.place(relx=0.50,rely=0.64,width=150,height=30)
    e6=Entry(win)
    e6.place(relx=0.50,rely=0.74,width=150,height=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f1=Frame(win,width=350,height=750,bg="pink")
    f1.place(relx=0.00,rely=0.06)
    f=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f2=Label(win,text="@swetha",font=label_font,bg="blue",fg="white")
    f2.place(relx=0.50,rely=0.94)
    f.place(relx=0.00,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Customer Registration",bg="green",fg="white",font=label_font,command=lambda:custreg(win))
    b.place(relx=0.04,rely=0.1)
    b1=Button(win,text="Admin Login",bg="green",fg="white",font=label_font,command=lambda:adminlog(win))
    b1.place(relx=0.04,rely=0.2)
    b2=Button(win,text="Customer Login",bg="green",fg="white",font=label_font,command=lambda:customerlog(win))
    b2.place(relx=0.04,rely=0.3)
    b3=Button(win,text="Exit",bg="green",fg="white",font=label_font,command=lambda:exit(win))
    b3.place(relx=0.04,rely=0.6)
    def insert():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="customer")
        cursor=connection.cursor()
        s="insert into student(Name,AdharNo,PanNo,Contact,EmailId,Address)values(%s,%s,%s,%s,%s,%s)"
        t=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo("registration","Insert Successfully")
    def update():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="customer")
        cursor=connection.cursor()
        sql= "update student set Adhar No='"+str(e2.get())+"',Pan No='"+str(e3.get())+"',Contact='"+str(e4.get())+"',Email Id='"+str(e5.get())+"',Address='"+str(e6.get())+"' where Name='"+str(e1.get())+"'"
        cursor.execute(sql)
        connection.commit()  
        messagebox.showinfo("registration","update successfull") 
    def delete():
        connection=mysql.connect(host="localhost",user="rooJt",password="livewire",database="customer")
        cursor=connection.cursor()
        sql="DELETE From student WHERE Name='"+e1.get()+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("registration","delete successfull")
        
    a=Button(win,text="Insert",font=label_font,bg="green",fg="white",command=lambda:insert())   
    a.place(relx=0.7,rely=0.3) 
    b=Button(win,text="Update",font=label_font,bg="green",fg="white",command=lambda:update())
    b.place(relx=0.7,rely=0.4)
    c=Button(win,text="Delete",font=label_font,bg="green",fg="white",command=lambda:delete())
    c.place(relx=0.7,rely=0.5)
    win.mainloop()

def home():
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    f=Frame(win,width=1500,height=60,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.5,rely=0.0)
    f1=Frame(win,width=1000,height=50,bg="green")
    f1.place(relx=0.45,rely=0.4)
    img=ImageTk.PhotoImage(Image.open("bank.jpg.jpg"))
    l=Label(f1,image=img)
    l.pack()
    f1=Frame(win,width=450,height=750,bg="pink")
    f1.place(relx=0.00,rely=0.06)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Customer Registration",bg="green",fg="white",font=label_font,command=lambda:custreg(win))
    b.place(relx=0.03,rely=0.1)
    b1=Button(win,text="Admin Login",bg="green",fg="white",font=label_font,command=lambda:adminlog(win))
    b1.place(relx=0.03,rely=0.2)
    b2=Button(win,text="Customer Login",bg="green",fg="white",font=label_font,command=lambda:customerlog(win))
    b2.place(relx=0.03,rely=0.3)
    b3=Button(win,text="Exit",bg="green",fg="white",font=label_font,command=lambda:exit(win))
    b3.place(relx=0.03,rely=0.6)
    f1=Frame(win,width=1500,height=60,bg="blue")
    f1.place(relx=0,rely=0.94)
    f2=Frame(win,width=1500,height=60,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f2=Label(win,text="@swetha",font=label_font,bg="blue",fg="white")
    f2.place(relx=0.50,rely=0.94)
    win.mainloop()


home()