# import tkinter
# top=tkinter.Tk()
# top.mainloop()
# from tkinter import*
# root=Tk()
# frame=Frame(root,bg="blue",width=800,height=100)
# frame.pack()
# root.mainloop()
# import tkinter
# t=tkinter.Tk()
# f=tkinter.Frame(t,bg="red",width=500,height=300)
# b=tkinter.Button(t,bg="blue")
# b.pack()
# f.pack()
# t.mainloop()
# import tkinter
# t=tkinter.Tk()
# f1=tkinter.Frame(t)
# f2=tkinter.Frame(t)
# L=tkinter.Label(f1,text="hello",bg="blue")
# L.pack()
# b=tkinter.Button(f2,text="livewire")
# b.pack()
# f1.pack(padx=100,pady=500)
# f2.pack(padx=250,pady=300)
# t.mainloop()
# from tkinter import*
# root=Tk()
# for fm in["orange","white","green"]:
#  Frame(height=20,width=30,bg=fm).pack()
#  root.mainloop()
# from tkinter import*
# master=Tk()
# W=Canvas(master,width=40,height=60)
# W.pack()
# Canvas_height=20
# Canvas_width=20
# y=int(Canvas_height/2)
# W.create_line(0,y,Canvas_width,y)
# mainloop()
# from tkinter import*
# master=Tk()
# var1=IntVar()
# Checkbutton(master,text="male",variable=var1).grid(row=0,sticky=W)
# var2=IntVar()
# Checkbutton(master,text="female",variable=var2).grid(row=1,sticky=W)
# mainloop()
# from tkinter import*
# master=Tk()
# Label(master,text="first Name").grid(row=0)
# Label(master,text="Last Name").grid(row=1)
# e1=Entry(master)
# e2=Entry(master)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# mainloop()
# from tkinter import*
# root=Tk()
# frame=Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side=BOTTOM)
# redbutton=Button(frame,text="red",fg="blue")
# redbutton.pack(side=LEFT)
# greenbutton=Button(frame,text="white",fg="green")
# greenbutton.pack(side=LEFT)
# bluebutton=Button(frame,text="blue",fg="yellow")
# bluebutton.pack(side=LEFT)
# blackbutton=Button(bottomframe,text="red",fg="red")
# blackbutton.pack(side=BOTTOM)
# root.mainloop()
# from tkinter import*
# top=Tk()
# Lb=Listbox(top)
# Lb.insert(1,"python")
# Lb.insert(2,"java")
# Lb.insert(3,"webdesign")
# Lb.insert(4,"any other")
# Lb.pack()
# top.mainloop()
# from tkinter import*                                                                                                                                                                                                                                                                                  
# root=Tk()
# root.title("welcome to Geek for Geeks")
# root.geometry("350x200")
# Lbl=Label(root,text="Are you a Geek?")
# Lbl.grid()
# txt=Entry(root,width=10)
# txt.grid(column=1,row=0)
# def clicked():
#     res="you wrote"+txt.get()                               
#     Lbl.configure(text=res)
# btn=Button(root,text="click me",fg="red",command=clicked)
# btn.grid(column=2,row=0)
# root.mainloop()   
# from tkinter import*
# root=Tk()
# menu=Menu(root)
# root.config(menu=menu)
# filemenu=Menu(menu)
# menu.add_cascade(label="file",menu=filemenu)
# filemenu.add_command (label="New")
# filemenu.add_command(label="Open...")
# filemenu.add_separator()
# filemenu.add_command(label="Exit",command=root.quit)
# helpmenu=Menu(menu)
# menu.add_cascade(label="Help",menu=helpmenu)
# helpmenu.add_command(label="About")
# root.mainloop()
# from tkinter import*
# main=Tk()
# ourMessage="this is our message"
# messagevar=Message(main,text=ourMessage)
# messagevar.config(bg="pink")
# messagevar.pack()
# main.mainloop()
# from tkinter import*
# root=Tk()
# v=IntVar()
# Radiobutton(root,text="GFG",variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text="MIT",variable=v,value=2).pack(anchor=W)
# mainloop()
# from tkinter import*
# master=Tk()
# w=Scale(master,from_=0,to=42)
# w.pack()
# mainloop()
# from tkinter import*
# root=Tk()
# Scrollbar=Scrollbar(root)
# Scrollbar.pack(side=RIGHT,fill=Y)
# mylist=Listbox(root,yscrollcommand=Scrollbar.set)
# for line in range(100):
#     mylist.insert(END,"livewire"+str(line))
# mylist.pack(side=LEFT,fill=BOTH)
# Scrollbar.config(command=mylist.yview)
# mainloop()
# from tkinter import*
# root=Tk()
# T=Text(root,height=2,width=30)
# T.pack()
# T.insert(END,"Monalisa is the\n name of famous\n painting")
# mainloop()
# from tkinter import*
# root=Tk()
# root.title("swetha")
# top=Toplevel()
# top.title("python")
# top.mainloop()
# from tkinter import*
# from PIL import ImageTk,Image
# from PIL.ImageTk import PhotoImage
# win=Tk()
# win.geometry("100x500")
# frame=Frame(win,width=600,height=400)
# frame.pack()
# frame.place(anchor="center",relx=0.5,rely=0.5)
# img=PhotoImage(Image.open("dog.jpg"))
# frame1=Frame(win,width=600,height=400)
# frame1.pack()
# frame1.place(anchor="w",relx=0.5,rely=0.5)
# img1=PhotoImage(Image.open("dogs.jpg"))
# label=Button(frame,image=img)
# label.pack()
# label1=Button(frame,image=img1)
# label1.pack()
# win.mainloop()
# import tkinter as tk
# root=tk.Tk()
# root.geometry("600x400")
#               name_vr=tk.StringVar()
# passw_var=tk.StringVar()
# def submit():
        # name=name_var.get()
        # password=passw_var.get() 
        # print("the name is:"+name)
        # print("the password is:"+password)
        # name_var.set("")
        # passw_var.set("")
        # name_label=tk.Label(root,text="username",font=("calibre",10,"normal"))
        # passw_label=tk.Label(root,text="password",font=("calibre",10,"bold"))
        # passw_entry=tk.Entry(root,textvariable=passw_var.font=("calibre",10,"normal"),show="*")
        # sub_btn=tk.Button(root,text="submit",command=submit)
        # name_label.grid(row=0,column)
# from tkinter import*
# r=Tk()
# r.geometry("400x400")
# l1=Label(r,text="enter the first value")
# l1.grid(row=0,column=1)
# l2=Label(r,text="enter the second value")
# l2.grid(row=1,column=1)
# l3=Label(r,text="result")
# l3.grid(row=2,column=1)
# e1=Entry(r)
# e1.grid(row=0,column=2)
# e2=Entry(r)
# e2.grid(row=1,column=2)
# e3=Entry(r)
# e3.grid(row=3,column=2)
# def add():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a+b
#     e3.insert(0,c)
# b=Button(r,text="Add",command=lambda:add())
# b.grid(row=4,column=3)
# def sub():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a-b
#     e3.insert(0,c)
# b=Button(r,text="sub",command=lambda:sub())
# b.grid(row=5,column=3)
# def mul():
#     a=int(e1.get())
#     b=int(e2.get())
#     c=a*b
#     e3.insert(0,c)
# b=Button(r,text="mul",command=lambda:mul())
# b.grid(row=6,column=3)
# r.mainloop()
# a=123456789
# a1=a
# c=0
# while(a1>0):
#     r=a1%10
#     c=(c*10)+r
#     a1=a1//10
# print(c)
# s=12
# s1=s*(s)
# print(s1)
# a=144
# a1(a)
# c=0
# while(a1>0):
#   r=a1%10
#   c=(c*10)+r
#   a1=a1//10
# print(c)
# if c==a:
#   print("it is adom number")
# else:
#   print("it is not adom number")
# sum=int(input("enter the value"))
# sum1=sum
# squ1=sum1*sum1
# firstvalue=153
# while(squ1>0):
#   r=squ1%10
#   sum1+=squ1**sum1
#   sum1=sum1//10
# if(firstvalue):
#   print ("amstong num")
# else:
#   print("not")
# store=int(input("enter the first value"))
# store1=store
# original=store1*store1
# firstvalue=0
# while(original>0):
#   s=original%10
#   firstvalue=(firstvalue*10)+s
#   original=original//10
# temperature=0
# while(store1>0):
#   s=store1%10
#   temperature+=temperature**0
#   store1=store1//10
# secondvalue=temperature*temperature
# if(firstvalue==secondvalue):
#   print("amstrong num")
# else:
#   print("not")
# dup=153
# temp=0
# while(dup>0):
#     r=dup%10
#     temp=temp+(r**3)
#     dup=dup//10
# if(dup):
#     print("amstrong num")
# else:
#     print("not")

# from mod import *
# if(reverse(square(12))==square(reverse(12))):
#     print("This is the Adam Number")
# else:
    # print("This is not a palindra


# x=int(input("enter the value:"))
# a=1
# b=1

# while(x>0):
#     c=a+b
#     a=b
#     b=c
#     x-=1
#     print(c)
# a=int(input("enter the value:"))
# if a%2==0:
#     print("even number",a+10)
# else:
#     print("odd number",a+25)
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# def mod(a,b):
#     print(a%b)

# c=1
# while(c==1):
#     n=int(input("enter your choice 1.add\n 2.sub\n 3.mul\n 4.div\n 5.mod\n"))
#     a=int(input("enter the first value:"))
#     b=int(input("enter the second value:"))
#     if(n==1):
#         add(a,b)
#     elif(n==2):
#         sub(a,b)
#     elif(n==3):
#         mul(a,b)
#     elif(n==4):
#         div(a,b)
#     elif(n==5):
#         mod(a,b)
#     else:
#         print("enter the correct input!!!!!!")
#         c=int(input("if you want continue,please enter 1!"))
# store=int(input("enter the value"))
# st1=store
# st2=st1*st1
# firstvalue=0
# while(st2>0):
#     r=st2%10
#     firstvalue=(firstvalue*10)+r
#     st2=st2//10
# temp=0
# while(st1>0):
#     r=st1%10
#     temp=(temp*10)+r
#     st1=st1//10
# secondvalue=temp*temp
# if(firstvalue==secondvalue):
#     print("adam number")
# else:
#     print("not")
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# num=5
# print("the factorial of",num,"is",factorial(num))
# x=int(input("enter the value:"))
# a=1
# b=1
# while(x>0):
#     c=a+b
#     a=b
#     b=c
#     x-=1
#     print(c)
# def amstrong(c):
#  num=c
# d=0
# while(num>0):
#     r=num%10
#     d=d+(r**3)
#     num=num//10
# print(d)
# if(d==c):
#     print("amstrong number")
# else:
#     print("not")
# a=str(input("enter your name:"))
# print(a[2])
# if(a[2]=="a"):
#     b=int(input("enter the value:"))
#     if b%2==0:
#         print("even number")
#     else:
#         print("odd number")
# elif(a[2]=="b"):
#     b=str(input("enter second number:"))
# else:
#     
# a="swetha"


# print(a[1:3].upper(),a[3:5].upper(),sep='***')

# a=[12,8,9,6,5]
# a.sort(reverse=a)
# p
# arint(a)
# a.sort()
# print(a)
# a=[3,1,2,55,23,11,9]
# b=a.copy()
# b.sort()
# if(a==b):
#  print(a)
# result=map(lambda x:x*2,a)
# print(list(result))
# else:
# print("opps")    

# n="swetha"
# for x in range(6):
#     print(n[:x])

# for x in range(12):
#     print()
#     for j in range(x):
#         print(j,end="")
# n=int(input("enter the value:"))
# for i in range(n):
#     for j in range(i+1):
#         if j==0 or i==j or i==n-1:
#             print("*" ,end=" ")
#         else:
#             print("*",end=" ")
#     print(" ")
# n=int(input("enter the value:"))
# for i in range(n):
#     if i==0 or i==n-1:
#         print("*",end=" ")
#     else:
#         print("*",end=" ")
#     print(" ")

# file=open("G.txt","a")
# name=str(input("enter name"))
# age=int(input("enter age"))
# fname=str(input("enter father name"))
# email=str(input("enter your email"))
# phn=int(input("enter phone no"))
# m1=int(input("tamil"))
# m2=int(input("eng"))
# m3=int(input("maths"))
# m4=int(input("science"))
# m5=int(input("social"))
# total=m1+m2+m3+m4+m5
# average=total/5
# print(total)
# print(average)
# file.close()
# if age>18:
#     print("eligible for age")
# elif total>35:
#     print("eligible the mark")
# else:
#     print("total and average")
# file=open("G.txt","a")
# file.write(name)
# file.write("\t")
# file.write(str(age))
# file.write("\t")
# file.write(fname)
# file.write("\t")
# file.write(email)
# file.write("\t")
# file.write(str(phn))
# file.write("\t")
# file.write(str(m1))
# file.write("\t")
# file.write(str(m2))
# file.write("\t")
# file.write(str(m3))
# file.write("\t")
# file.write(str(m4))
# file.write("\t")
# file.write(str(m5))
# file.write("\t")
# file.write(str(total))
# file.write("\t")
# file.write(str(average))
# file.write("\t")
# file.close()

from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk, Image
import os


def customerloginpage(data,win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    f1=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.5,rely=0.5)
    f1.pack()
    frame1=Frame(win,width=400,height=470,bg="yellow")
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
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="swetha",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.36,rely=0.45)
    win.mainloop()


def  customerlogin1(a,b,win):

    if os.path.exists('bank.jpg.jpg'):
        with open('bank.jpg.jpg','r') as file:
            lines=file.readlines()
            for x in lines:  
                x1=x.split("\t")            
                username1=x1[0]
                password1=x1[3]
                if(username1==a and password1==b):
                    customerloginpage(x1,win)
                
def customerlog(win):
    win.destroy()
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    frame1=Frame(win,width=400,height=250,bg="violet")
    frame1.place(relx=0.35,rely=0.35)
    
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f1=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.40,rely=0.5)
    f1.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b2=Label(win,text="Customer Login",bg="green",fg="white",font=label_font)
    b2.place(relx=0.43,rely=0.23)

    label_font=font.Font(win,weight="bold",family="Times New Roman",size=15)
    l=Label(win,text="Customer ID",font=label_font).place(relx=0.37,rely=0.41)
    l=Label(win,text="Password",font=label_font).place(relx=0.37,rely=0.51)
    e1=Entry(win)
    e1.place(relx=0.49,rely=0.41,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.49,rely=0.51,width=150,height=30)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",bg="green",font=label_font,command=lambda:customerlogin1(e1.get(),e2.get(),win))
    b.place(relx=0.49,rely=0.60)
    
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="swetha",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.38,rely=0.90)
    win.mainloop()

def custreg(win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    frame1=Frame(win,width=400,height=530,bg="violet")
    frame1.place(relx=0.35,rely=0.20)
    f=Frame(win,width=1500,height=500,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.40,rely=0.5)
    f.pack()

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
    
    def file(a,b,c,d,win):
        f=open('g.txt','a')
        f.write('\n')
        f.write(e1.get())
        f.write('\t')
        f.write(str(e2.get()))
        f.write('\t')
        f.write(str(e3.get()))
        f.write('\t')
        f.write(str(e4.get()))
        f.write('\t')
        f.write(e5.get())
        f.write('\t')
        f.write(str(e6.get()))
        f.write('\t')

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Register",bg="green",fg="white",font=label_font,command=lambda:file(e1.get(),e2.get(),e3.get(),e4.get(),win))
    b.place(relx=0.50,rely=0.80)
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="swetha",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.40,rely=0.93)
    win.mainloop()

def adminpage(win):
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    f=Frame(win,width=1500,height=50,bg="blue")
    f.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f1=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f1.place(relx=0.40,rely=0.3)
    f1.pack()
    frame1=Frame(win,width=400,height=480,bg="pink")
    frame1.place(relx=0.35,rely=0.25)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Admin Page",bg="green",fg="white",font=label_font)
    b.place(relx=0.45,rely=0.18)

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="Name",font=label_font).place(relx=0.38,rely=0.26)
    l2=Label(win,text="Aadhar No",font=label_font).place(relx=0.38,rely=0.36)
    l3=Label(win,text="Pan No",font=label_font).place(relx=0.38,rely=0.46)
    l4=Label(win,text="Contact",font=label_font).place(relx=0.38,rely=0.56)
    l5=Label(win,text="Email ID",font=label_font).place(relx=0.38,rely=0.66)
    l6=Label(win,text="Address",font=label_font).place(relx=0.38,rely=0.76)
    e1=Entry(win)
    e1.place(relx=0.50,rely=0.27,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.50,rely=0.37,width=150,height=30)
    e3=Entry(win)
    e3.place(relx=0.50,rely=0.47,width=150,height=30)
    e4=Entry(win)
    e4.place(relx=0.50,rely=0.57,width=150,height=30)
    e5=Entry(win)
    e5.place(relx=0.50,rely=0.67,width=150,height=30)
    e6=Entry(win)
    e6.place(relx=0.50,rely=0.77,width=150,height=30)

   
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",bg="green",font=label_font,command=lambda:adminlogin(e1.get(),e2.get(),win))
    b.place(relx=0.50,rely=0.83,width=150,height=30)


    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="swetha",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.40,rely=0.93)
    win.mainloop()


def adminlogin(a,b,win):
    win.destroy()
    if(a=="swetha" and b=="vedha"):
        adminpage(win)
    else:
        print("invalid username or password")
    

def adminlog(win):
    win.destroy()
    win=Tk()
    win.attributes('-fullscreen',True)
    win.geometry("500x500")
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    
    frame1=Frame(win,width=400,height=250,bg="violet")
    frame1.place(relx=0.35,rely=0.35)

    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="Indian Bank",font=label_font,bg="blue",fg="white")
    f.place(relx=0.40,rely=0.5)
    f.pack()

    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Label(win,text="Admin Login",bg="green",fg="white",font=label_font)
    b.place(relx=0.44,rely=0.22)
  
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    l1=Label(win,text="UserName",font=label_font).place(relx=0.36,rely=0.40)
    l2=Label(win,text="Password",font=label_font).place(relx=0.36,rely=0.50)
   
    e1=Entry(win)
    e1.place(relx=0.52,rely=0.40,width=150,height=30)
    e2=Entry(win)
    e2.place(relx=0.52,rely=0.50,width=150,height=30)
    
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(win,text="Login",bg="green",font=label_font,command=lambda:adminlogin(e1.get(),e2.get(),win))
    b.place(relx=0.52,rely=0.58)
    f2=Frame(win,width=1500,height=50,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f2=Label(win,text="swetha",font=label_font,bg="blue",fg="white")
    f2.pack()
    f2.place(relx=0.38,rely=0.90)
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
    f.place(relx=0.00,rely=0.1)
    f.pack()
    f1=Frame(win,width=1000,height=50,bg="green")
    f1.place(relx=0.335,rely=0.35)
    img=ImageTk.PhotoImage(Image.open("bank.jpg.jpg"))
    l=Label(f1,image=img)
    l.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=19)
    s="""Indian Bank is an Indian public sector bank, established in 1907 
    and headquartered in Chennai.Total business of the bank has touched ₹1,094,75 
    crore(US$140 billion) as onfMarch 231, 023."""
    l1=Label(win,text=s,font=label_font)
    l1.place(relx=0.206,rely=0.2)
    f1=Frame(win,width=350,height=750,bg="violet")
    f1.place(relx=0.00,rely=0.06)
    b=Button(win,text="Customer Registration",bg="green",fg="white",font=label_font,command=lambda:custreg(win))
    b.place(relx=0.00,rely=0.2)
    b1=Button(win,text="Admin Login",bg="green",fg="white",font=label_font,command=lambda:adminlog(win))
    b1.place(relx=0.00,rely=0.4)
    b2=Button(win,text="Customer Login",bg="green",fg="white",font=label_font,command=lambda:customerlog(win))
    b2.place(relx=0.00,rely=0.6)
    b3=Button(win,text="Exit",bg="green",fg="white",font=label_font,command=lambda:exit(win))
    b3.place(relx=0.1,rely=0.8)
    f2=Frame(win,width=1500,height=50,bg="blue")
    f2.place(relx=0,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f3=Label(win,text="swetha",font=label_font,bg="blue",fg="white")
    f3.place(relx=0.47,rely=0.94)
    win.mainloop()
home()



